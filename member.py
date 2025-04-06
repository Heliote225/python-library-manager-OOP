from user import User

class Member(User):
    def get_user_type(self):
        return "Member"