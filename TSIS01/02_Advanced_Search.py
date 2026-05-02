import psycopg2
from config import load_config

def search_advanced(page, limit, filter_group, search_email, sort_by):
    params = load_config()
    offset = (page - 1) * limit
    sql = f"""
    SELECT p.username, p.email, p.birthday, g.name 
    FROM phonebooktable p
    LEFT JOIN groups g ON p.group_id = g.id
    WHERE p.email ILIKE %s
    """
    query_params = [f"%{search_email}%"]
    if filter_group:
        sql += " AND g.name = %s"
        query_params.append(filter_group)
    sql += f" ORDER BY {sort_by} ASC LIMIT %s OFFSET %s;"
    query_params.extend([limit, offset])

    conn = None
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(query_params))
                return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Database Error: {error}")
        return []
    finally:
        if conn: conn.close()

def main():
    page = 1
    limit = 3
    filter_group = None
    search_email = ""
    sort_by = "username"

    while True:
        rows = search_advanced(page, limit, filter_group, search_email, sort_by)
        print(f"Page {page} | Sort: {sort_by} | Group: {filter_group or 'All'} | Email: '{search_email}'")
        if rows:
            for row in rows:
                print(f"Name: {row[0]:<15} | Email: {row[1]:<20} | B/D: {row[2]} | Group: {row[3]}")
        else:
            print("No contacts found on this page.")
        print("Commands: [n]ext, [p]rev, [f]ilter group, [s]earch email, [o]rder, [q]uit")
        cmd = input("Choice: ").strip().lower()

        if cmd == 'n':
            page += 1
        elif cmd == 'p':
            page = max(1, page - 1)
        elif cmd == 'f':
            filter_group = input("Enter group (Family/Work/Friend/Other) or 'clear': ").capitalize()
            if filter_group == 'Clear': filter_group = None
            page = 1
        elif cmd == 's':
            search_email = input("Enter partial email search: ")
            page = 1
        elif cmd == 'o':
            print("Sort by: [1] Name, [2] Birthday, [3] Date Added")
            choice = input("Select number: ")
            sort_map = {"1": "username", "2": "birthday", "3": "p.id"}
            sort_by = sort_map.get(choice, "username")
            page = 1
        elif cmd == 'q' or cmd == 'quit':
            print("Exiting...")
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()