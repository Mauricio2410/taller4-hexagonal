from app.application.ports.user_repository import UserRepository

class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def save(self, user):
        self.users[user.idusuario] = user
        return user

    def get_all(self):
        return list(self.users.values())

    def get_by_id(self, user_id):
        return self.users.get(user_id)

    def update(self, user_id, user_data):
        if user_id in self.users:
            self.users[user_id] = user_data
            return user_data
        return None

    def delete(self, user_id):
        return self.users.pop(user_id, None)