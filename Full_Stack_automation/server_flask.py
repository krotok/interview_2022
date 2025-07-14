from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример базы данных (в памяти)
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]

# Эндпоинт для получения всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Эндпоинт для добавления пользователя
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

# Эндпоинт для получения пользователя по ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)