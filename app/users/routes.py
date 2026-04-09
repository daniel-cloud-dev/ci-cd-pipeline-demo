from flask import Blueprint, jsonify
from app.users.services import list_users


users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
def get_users():
    users = list_users()
    return jsonify(users)
