class Judge():
    def __init__(self):
        self.__logindata = {}

    def check_account(self, account, password):
        if account in self.__logindata:
            if self.__logindata[account] == password:
                return True

            else:
                print("密码不正确")
                return False
        print("无此账号")
        return False
    def uid_judge(self):
        pass
    def create_account(self):
        pass
