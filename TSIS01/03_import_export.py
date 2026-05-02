import psycopg2
import csv
import json
from config import load_config

def get_group_id(cur, group_name):
    """Helper to get group_id from name or default to 'Other'."""
    if not group_name:
        group_name = 'Other'
    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    result = cur.fetchone()
    return result[0] if result else None

def export_json():
    path = input("Enter filename to save (e.g., contacts.json): ")
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Get main contact info
                cur.execute("""
                    SELECT p.username, p.email, p.birthday, g.name 
                    FROM phonebooktable p
                    LEFT JOIN groups g ON p.group_id = g.id
                """)
                contacts = cur.fetchall()
                
                data = []
                for contact in contacts:
                    name, email, bday, g_name = contact
                    cur.execute("SELECT phone, type FROM phones WHERE contact_username = %s", (name,))
                    phones = [{"phone": p[0], "type": p[1]} for p in cur.fetchall()]
                    
                    data.append({
                        "username": name,
                        "email": email,
                        "birthday": str(bday) if bday else None,
                        "group": g_name,
                        "phones": phones
                    })
                
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                print(f"--- Exported {len(data)} contacts to {path} ---")
    except Exception as e:
        print(f"Export Error: {e}")

def import_json():
    path = input("Enter JSON filename to import: ")
    config = load_config()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for entry in data:
                    name = entry['username']

                    cur.execute("SELECT 1 FROM phonebooktable WHERE username = %s", (name,))
                    if cur.fetchone():
                        choice = input(f"Duplicate found for '{name}'. [s]kip or [o]verwrite? ").lower()
                        if choice == 's': continue
                        cur.execute("DELETE FROM phones WHERE contact_username = %s", (name,))
                        cur.execute("DELETE FROM phonebooktable WHERE username = %s", (name,))

                    g_id = get_group_id(cur, entry.get('group'))
                    cur.execute("""
                        INSERT INTO phonebooktable (username, email, birthday, group_id)
                        VALUES (%s, %s, %s, %s)
                    """, (name, entry.get('email'), entry.get('birthday'), g_id))
                    
                    for p in entry.get('phones', []):
                        cur.execute("INSERT INTO phones (contact_username, phone, type) VALUES (%s, %s, %s)",
                                    (name, p['phone'], p['type']))
                print("JSON Import Successful")
    except Exception as e:
        print(f"Import Error: {e}")

def import_csv():
    path = input("Enter CSV filename (e.g., data.csv): ")
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(path, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        g_id = get_group_id(cur, row['group'])
                        cur.execute("""
                            INSERT INTO phonebooktable (username, email, birthday, group_id)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (username) DO UPDATE SET
                            email = EXCLUDED.email, birthday = EXCLUDED.birthday, group_id = EXCLUDED.group_id
                        """, (row['username'], row['email'], row['birthday'], g_id))
                        cur.execute("INSERT INTO phones (contact_username, phone, type) VALUES (%s, %s, %s)",
                                    (row['username'], row['phone'], row['phone_type']))
                print("--- CSV Import Successful ---")
    except Exception as e:
        print(f"CSV Error: {e}")

def main():
    while True:
        print("1. Export to JSON")
        print("2. Import from JSON")
        print("3. Import from CSV (Extended)")
        print("4. Exit")
        choice = input("What to do? ")
        
        if choice == '1': export_json()
        elif choice == '2': import_json()
        elif choice == '3': import_csv()
        elif choice == '4': break
        else: print("Invalid choice")

if __name__ == '__main__':
    main()