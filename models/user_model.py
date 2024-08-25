class User:
    users_db = []  # Usando una lista en memoria para simplificación

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @classmethod
    def get_all_users(cls):
        return cls.users_db

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users_db:
            if user.user_id == user_id:
                return user
        return None

    @classmethod
    def create_user(cls, user_data):
        new_user = User(user_data['user_id'], user_data['name'], user_data['email'])
        cls.users_db.append(new_user)
        return new_user

    @classmethod
    def update_user(cls, user_id, user_data):
        user = cls.get_user_by_id(user_id)
        if user:
            user.name = user_data['name']
            user.email = user_data['email']
            return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        user = cls.get_user_by_id(user_id)
        if user:
            cls.users_db.remove(user)
            return True
        return False
