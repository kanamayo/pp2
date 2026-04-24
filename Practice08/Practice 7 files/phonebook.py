import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database """
    # We wrap the SQL string in a list [] so the 'for' loop treats it as one command
    commands = [
        """
        CREATE TABLE IF NOT EXISTS phonebooktable (
            username VARCHAR(255),
            phone VARCHAR(255)
        )
        """
    ]
    
    conn = None
    try:
        print("Connecting to the PostgreSQL database...")
        params = load_config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # 3. Execute each command in the list
                for command in commands:
                    cur.execute(command)
                print("Table 'phonebookTable' verified/created successfully!")
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error occurred: {error}")
    
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':
    create_tables()