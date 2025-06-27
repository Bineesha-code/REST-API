# Task-4
# REST API with Flask
# Author: Bineesha K P
# Date: 27-06-2025

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data
users = {
    1: {"name": "Bini", "email": "bini@gmail.com"},
    2: {"name": "Anu", "email": "anu@gmail.com"}
}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email required"}), 400

    new_id = max(users.keys(), default=0) + 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"message": "User created", "id": new_id}), 201

# PUT - update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify({"message": "User updated"})

# DELETE - remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
