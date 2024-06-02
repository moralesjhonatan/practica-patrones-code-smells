from user_entity import UserEntity

class UserRepository:

    def getUser(self, userId):
        return UserEntity(1, 'Yonatan', 'yonatan@gmail.com')

    #def getUser(self, userId):
        # cursor = self.db.cursor()
        # cursor.execute("SELECT * FROM users WHERE id = %s", (userId,))
        # result = cursor.fetchone()
        # return {'name': result[1], 'email': result[2]}