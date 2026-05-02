import psycopg2
from config import load_config

def insert_user(name, phone):
    params = load_config()
    sql = """   
    INSERT INTO phonebooktable (username, phone)
    VALUES (%s, %s)
    ON CONFLICT (username) 
    DO UPDATE SET phone = EXCLUDED.phone;
    """
    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                if cur.rowcount > 0:
                    print(f"Successful: {name}")
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def main():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    
    if name and phone:
        insert_user(name, phone)
    else:
        print("Error: Name and phone are required. Invalid format")

if __name__ == '__main__':
    main()