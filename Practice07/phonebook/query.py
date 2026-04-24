import psycopg2
from config import load_config

def query_contacts(filter_type, search_term):
    params = load_config()
    conn = None
    if filter_type == '1': # Search by Name
        sql = "SELECT * FROM phonebooktable WHERE username ILIKE %s"
        query_param = f"%{search_term}%" 
    elif filter_type == '2': # Search by Phone Prefix
        sql = "SELECT * FROM phonebooktable WHERE phone LIKE %s"
        query_param = f"{search_term}%"
    else:
        print("Invalid filter selection.")
        return

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (query_param,))
                rows = cur.fetchall()
                print(f"\nFound {len(rows)} contact(s):")
                for row in rows:
                    print(f"User: {row[0]} | Phone: {row[1]}")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()
def main():
    print("1. Search by Name")
    print("2. Search by Phone Prefix")
    choice = input("Select filter (1 or 2): ").strip()
    term = input("Enter what to search: ").strip()
    if choice and term:
        query_contacts(choice, term)
    else:
        print("Selection and search term are required.")

if __name__ == '__main__':
    main()