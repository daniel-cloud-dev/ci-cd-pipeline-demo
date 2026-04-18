import psycopg2, time
from flask import current_app

def get_connection():
    for _ in range(5):
        try:
            return psycopg2.connect(
                host=current_app.config["DB_HOST"],
                database=current_app.config["DB_NAME"],
                user=current_app.config["DB_USER"],
                password=current_app.config["DB_PASSWORD"]
            )
        except psycopg2.OperationalError:
            time.sleep(2)
    raise Exception("DB not available")