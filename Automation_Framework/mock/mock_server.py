# ─────────────────────────────────────────────────────────
# 📂 mock/mock_server.py
from flask import Flask, jsonify, request as flask_request

def create_app():
    app = Flask(__name__)

    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        return jsonify({"id": user_id, "name": f"User{user_id}"}), 200

    @app.route("/users", methods=["POST"])
    def create_user():
        data = flask_request.json
        return jsonify({"id": 999, **data}), 201

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5001)