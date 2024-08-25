from flask import jsonify

def user_response(user):
    return jsonify({
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email
    })

def users_response(users):
    return jsonify([{
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email
    } for user in users])