from user_controller import UserController
from user_service import UserService

def main():
    user = UserController(UserService)
    user.getUser(1)
    print(user)

if __name__ == "__main__":
    main()