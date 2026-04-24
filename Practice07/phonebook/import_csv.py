import psycopg2
import csv
from config import load_config

def insert_from_csv(csvpath):
    sql = """INSERT INTO phonebooktable(username, phone)
             VALUES(%s, %s);"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                with open(csvpath, 'r', encoding='utf-8-sig') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        cur.execute(sql, row)
                    print("Data inserted successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    insert_from_csv("data.csv")