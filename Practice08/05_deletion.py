import psycopg2
from config import load_config

def setup_db_and_procedure():
    params = load_config()
    sql = """
    CREATE OR REPLACE FUNCTION delete_entry(p_name TEXT, p_phone TEXT)
    RETURNS INTEGER AS $$
    DECLARE
        rows_deleted INTEGER;
    BEGIN
        DELETE FROM phonebooktable 
        WHERE (username = p_name AND p_name <> '')
           OR (phone = p_phone AND p_phone <> '');
        GET DIAGNOSTICS rows_deleted = ROW_COUNT;
        RETURN rows_deleted;
    END;
    $$ LANGUAGE plpgsql;
    """
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
def main():
    setup_db_and_procedure()
    params = load_config()
    print("Enter the Name OR Phone to delete. Or 'exit' to quit")
    while True:
        target_name = input("\nUsername to delete (leave empty to skip): ").strip()
        if target_name.lower() == 'exit': break
        target_phone = input("Phone to delete (leave empty to skip): ").strip()
        if target_phone.lower() == 'exit': break
        if not target_name and not target_phone:
            print("Action cancelled: provide at least one thing.")
            continue
        try:
            with psycopg2.connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT delete_entry(%s, %s);", (target_name, target_phone))
                    count = cur.fetchone()[0]
                    if count > 0:
                        print(f"Success: {count} deleted.")
                    else:
                        print("No matching found")
                    conn.commit()
        except Exception as e:
            print(f"Database Error: {e}")

if __name__ == '__main__':
    main()