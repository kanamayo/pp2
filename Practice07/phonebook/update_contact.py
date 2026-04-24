import psycopg2
from config import load_config

def update_phone(username, new_phone):
    sql = """
        UPDATE phonebooktable
        SET phone = %s
        WHERE username = %s
    """
    params = load_config()
    conn = None
    updated_rows = 0
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone, username))
                updated_rows = cur.rowcount
                if updated_rows > 0:
                    print(f"Successfully updated {updated_rows} record(s).")
                else:
                    print(f"No contact found with the name '{username}'.")

    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def main():
    target_name = input("Enter the username you want to update: ").strip()
    new_number = input(f"Enter the new phone number for {target_name}: ").strip()

    if target_name and new_number:
        update_phone(target_name, new_number)
    else:
        print("Error: Both name and new number are required.")

if __name__ == '__main__':
    main()