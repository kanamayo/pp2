import psycopg2
from config import load_config

def update_schema():
    sql = [
        """
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        INSERT INTO groups (name) 
        VALUES ('Family'), ('Work'), ('Friend'), ('Other')
        ON CONFLICT (name) DO NOTHING
        """,
        """
        ALTER TABLE phonebooktable 
        ADD COLUMN IF NOT EXISTS email VARCHAR(100),
        ADD COLUMN IF NOT EXISTS birthday DATE,
        ADD COLUMN IF NOT EXISTS group_id INTEGER REFERENCES groups(id)
        """,
        """
        CREATE TABLE IF NOT EXISTS phones (
            id SERIAL PRIMARY KEY,
            contact_username VARCHAR(255), 
            phone VARCHAR(20) NOT NULL,
            type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
        )
        """
    ]

    conn = None
    try:
        params = load_config()
        
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                for command in sql:
                    cur.execute(command)
                print("Database schema successfully extended to the 'Extended Contact Model'!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error occurred during migration: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':
    update_schema()