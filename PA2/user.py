class User():
    def __init__(self, account_number: str, password: str, name: str, id_ , corse: list):
        self.name = name
        self.account = account_number
        self.__password = password

    def login(self):
        return self.account, self.__password
