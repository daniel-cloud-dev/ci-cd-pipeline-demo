import psycopg2, flask
from flask import current_app


def get_connection():
    return psycopg2.connect(
        host=current_app.config["DB_HOST"],
        database=current_app.config["DB_NAME"],
        user=current_app.config["DB_USER"],
        password=current_app.config["DB_PASSWORD"]
)

#conexão com o PostgreSQL