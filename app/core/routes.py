from flask import Blueprint

home_bp = Blueprint("core", __name__)

@home_bp.route("/", methods=["GET"])
def index():
    return {"status": "ok"}
