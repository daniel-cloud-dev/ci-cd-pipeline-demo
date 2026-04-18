from flask import Flask
from .users.routes import users_bp
from .health.routes import health_bp
from .core.routes import home_bp
import os

def create_app(config_class="app.config.DevConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["DB_HOST"] = os.getenv("DB_HOST")
    app.config["DB_NAME"] = os.getenv("DB_NAME")
    app.config["DB_USER"] = os.getenv("DB_USER")
    app.config["DB_PASSWORD"] = os.getenv("DB_PASSWORD")

    app.register_blueprint(home_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(health_bp)

    return app