from flask import Blueprint, request, jsonify
from models.user_model import User
from views.user_view import user_response, users_response

user_blueprint = Blueprint('user_controller', __name__)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.get_all_users()
    return users_response(users), 200

@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return user_response(user), 200
    return jsonify({'message': 'User not found'}), 404

@user_blueprint.route('/', methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_user = User.create_user(user_data)
    return user_response(new_user), 201

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    updated_user = User.update_user(user_id, user_data)
    if updated_user:
        return user_response(updated_user), 200
    return jsonify({'message': 'User not found'}), 404

@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if User.delete_user(user_id):
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404