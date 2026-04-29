from flask import request, jsonify


users = {}


def add_user(user_id, name, age):
    user = {
        "id": user_id,
        "name": name,
        "age": age
    }
    users[user_id] = user
    return user


def get_user(user_id):
    return users[user_id]


def delete_user(user_id):
    del users[user_id]
    return "User deleted"


def calculate_average_age():
    total = 0
    for user in users:
        total += user["age"]
    return total / len(users)


def find_user_by_name(name):
    for user_id in users:
        if users[user_id]["name"] = name:
            return users[user_id]
    return None


def get_adult_users():
    adults = []
    for user_id, user in users.items:
        if user["age"] >= 18:
            adults.append(user)
    return adults


def update_user_age(user_id, new_age):
    if user_id in users:
        users[user_id]["age"] == new_age
        return users[user_id]
    return None


def divide_users_into_groups(group_size):
    user_list = list(users.values())
    groups = []
    for i in range(0, len(user_list), group_size):
        groups.append(user_list[i:i + group_size + 1])
    return groups


def handle_request():
    data = request.get_json()
    user_id = data["id"]
    name = data["name"]
    age = data["age"]
    new_user = add_user(user_id, name, age)
    return jsonify(new_user)
