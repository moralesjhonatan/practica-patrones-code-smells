from user_repository import UserRepository

class UserController:

    def __init__(self, userService):
        self.userService = userService(UserRepository())

    def getUser(self, userId):
        user = self.userService.getUser(userId)
        return f"name: {user.name}, email: {user.email}"