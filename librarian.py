from user import User

class Librarian(User):
    def get_user_type(self):
        return "Librarian"