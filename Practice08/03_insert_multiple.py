import psycopg2
from config import load_config

def insert_multiple(name, phone):
    params = load_config()
    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM insert_multiple(ARRAY[%s], ARRAY[%s]);", (name, phone))
                bad_data = cur.fetchone()
                if bad_data:
                    print(f"Invalid Format: {bad_data[1]} (Not saved)")
                else:
                    print(f"Successful: {name}")
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
    finally:
        if conn is not None:
            conn.close()

def main():
    params = load_config()
    sql = """
    CREATE OR REPLACE FUNCTION insert_multiple(p_names TEXT[], p_phones TEXT[])
    RETURNS TABLE (err_name TEXT, err_phone TEXT) AS $$
    DECLARE i INTEGER;
    BEGIN
        FOR i IN 1 .. array_upper(p_names, 1) LOOP
            IF p_phones[i] ~ '^[0-9]+$' THEN
                INSERT INTO phonebooktable (username, phone)
                VALUES (p_names[i], p_phones[i])
                ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;
            ELSE
                err_name := p_names[i];
                err_phone := p_phones[i];
                RETURN NEXT;
            END IF;
        END LOOP;
    END;
    $$ LANGUAGE plpgsql;
    """
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    querying = True
    while querying:
        name = input("Enter name (or 'exit'): ")
        if name == 'exit':
            print("Exit queried. Exiting...")
            break
        phone = input("Enter phone: ")
        
        if name and phone:
            insert_multiple(name, phone)
        else:
            print("Error: Name and phone are required.")

if __name__ == '__main__':
    main()