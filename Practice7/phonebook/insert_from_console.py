import psycopg2
from config import load_config

def insert_user(username, phone):
    """ Insert a single user into the phonebooktable """
    sql = "INSERT INTO phonebooktable(username, phone) VALUES(%s, %s)"
    params = load_config()
    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, phone))
                print(f"Successfully added {username} to the phonebook.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def main():
    while True:
        name = input("\nEnter username (or type 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            break
        number = input(f"Enter phone number for {name}: ").strip()
        if not name or not number:
            print("Error: Both name and phone number are required!")
            continue
        insert_user(name, number)
    print("\nExiting. Have a great day!")
if __name__ == '__main__':
    main()