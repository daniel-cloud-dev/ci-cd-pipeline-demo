from flask import Flask
from app.users.routes import users_bp
from app.health.routes import health_bp

def create_app(config_class="app.config.DevConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(users_bp)
    app.register_blueprint(health_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)