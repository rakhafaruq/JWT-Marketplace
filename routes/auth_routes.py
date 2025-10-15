from flask import Blueprint, request, jsonify
from utils.jwt_utils import create_jwt

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

USERS = {
    "user1@example.com": {"password": "pass123", "name": "BUDI"}
}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = USERS.get(email)
    if user and user.get("password") == password:
        token = create_jwt(email)
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
