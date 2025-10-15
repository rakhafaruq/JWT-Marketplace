from flask import Blueprint, request, jsonify
from utils.jwt_utils import verify_jwt_from_request
from routes.auth_routes import USERS

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["PUT"])
def update_profile():
    decoded, error_response, status = verify_jwt_from_request(request)
    if error_response:
        return error_response, status

    user_email = decoded.get("email")
    user = USERS.get(user_email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json(silent=True) or {}
    name = data.get("name")
    new_email = data.get("email")

    if name:
        user["name"] = name
    if new_email:
        USERS[new_email] = USERS.pop(user_email)
        user_email = new_email

    return jsonify({
        "message": "Profile updated",
        "profile": {"name": user["name"], "email": user_email}
    }), 200
