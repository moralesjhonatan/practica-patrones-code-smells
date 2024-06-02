from user import User

class UserService:

    def __init__(self, userRepository):
        self.userRepository = userRepository

    def getUser(self, userId):
        user = self.userRepository.getUser(userId)
        return User(user.name, user.email)