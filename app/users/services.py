from app.users.repository import get_all_users

def list_users():
    rows = get_all_users()
    return [{"id": r[0], "name": r[1]} for r in rows]