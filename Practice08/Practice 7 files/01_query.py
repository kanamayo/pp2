import psycopg2
from config import load_config

def query(q):
    params = load_config()
    conn = None
    sql = "SELECT * FROM phonebooktable WHERE username LIKE %s OR phone ILIKE %s"
    query_param = f"%{q}%"
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute (sql, (query_param, query_param))
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
    que = input("Enter a query: ")
    query(que)

if __name__ == '__main__':
    main()