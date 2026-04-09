class BaseConfig:
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_NAME = "mydb"
    DB_USER = "postgres"
    DB_PASSWORD = "postgres"


class TestConfig(BaseConfig):
    TESTING = True
    DB_HOST = "test_db"
    DB_NAME = "test_name"
    DB_USER = "test_user"
    DB_PASSWORD = "test_ps"

class DevConfig(BaseConfig):
    DEBUG = True