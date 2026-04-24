import psycopg2
from config import load_config

def delete_contact(identifier_type, value):
    """ Delete a contact by username or phone number """
    params = load_config()
    conn = None
    
    # Select the correct column for the WHERE clause
    if identifier_type == '1':
        sql = "DELETE FROM phonebooktable WHERE username = %s"
    elif identifier_type == '2':
        sql = "DELETE FROM phonebooktable WHERE phone = %s"
    else:
        print("Invalid option selected.")
        return

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (value,))
                rows_deleted = cur.rowcount
                if rows_deleted > 0:
                    print(f"Successfully deleted {rows_deleted} contact(s).")
                else:
                    print(f"No contact found matching '{value}'.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()
def main():
    print("--- Delete Contact ---")
    print("1. Delete by Username")
    print("2. Delete by Phone Number")
    choice = input("Select option (1 or 2): ").strip()
    target = input("Enter the name or number to delete: ").strip()
    if choice and target:
        delete_contact(choice, target)
    else:
        print("All fields are required.")

if __name__ == '__main__':
    main()