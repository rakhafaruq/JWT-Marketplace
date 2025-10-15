from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from routes.auth_routes import auth_bp
from routes.items_routes import item_bp
from routes.profile_routes import profile_bp

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(profile_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
