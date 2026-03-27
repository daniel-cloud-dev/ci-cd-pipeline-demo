from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({
            "status": "ok",
            "message": "API is running!"
        }), 200

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy"
        }), 200

    @app.route("/users")
    def users():
        return jsonify([
            {"id": 1, "name": "Ana"},
            {"id": 2, "name": "Bruno"},
            {"id": 3, "name": "Carlos"},
        ])

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)