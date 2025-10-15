from flask import Blueprint, jsonify

item_bp = Blueprint("items", __name__)

@item_bp.route("/items", methods=["GET"])
def get_items():
    items = [
        {"id": 1, "name": "Kemeja Hitam", "price": 150000},
        {"id": 2, "name": "Celana Jorts", "price": 220000},
        {"id": 3, "name": "Sepatu Hitam", "price": 250000}
    ]
    return jsonify({"items": items}), 200
