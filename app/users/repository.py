from app.db import get_connection

def get_all_users():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM users;")
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()