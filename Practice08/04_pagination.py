import psycopg2
from config import load_config

def pagination(page_num, limit=3):
    params = load_config()
    offset = (page_num - 1) * limit
    sql = """
    SELECT username, phone 
    FROM phonebooktable 
    ORDER BY username ASC 
    LIMIT %s OFFSET %s;
    """
    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit, offset))
                rows = cur.fetchall()
                if rows:
                    print(f"\nShowing Page {page_num}")
                    for row in rows:
                        print(f"Name: {row[0]:<20} | Phone: {row[1]}")
                else:
                    print(f"\n[!] Page {page_num} is empty.")
                    
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def main():
    while True:
        user_input = input("\nEnter page number to view (or 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break
            
        if user_input.isdigit():
            page = int(user_input)
            if page > 0:
                pagination(page)
            else:
                print("Enter a page number greater than 0.")
        else:
            print("Invalid input, enter a number")

if __name__ == '__main__':
    main()