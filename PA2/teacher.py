from user import User
class Teacher(User):
    def __init__(self, name: str, account_number: str, password: str):
        super().__init__(name, account_number, password)
        self.jurisdiction = "teacher"