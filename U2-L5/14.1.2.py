class User:
    def __init__(self, id_ = "1", nickname = "2", credits = "3"):
        self.id_ = id_
        self.nickname = nickname
        self.credits = credits

    def get_info(self):
        print("id=", self.id_, "\n nickname =", self.nickname, "\n credits = ", credits)

    def upgrade_to_vip(self,vip_level):
        return Vip(self.id_,vip_level=1)

    pass

class Vip(User):
    def __init__(self,vip_level = "1"):
        super(Vip, self).__init__()
        self.vip_level = "6"
    def get_info(self):
        return print('\n'.join(['{0}: {1}'.format(item[0], item[1]) for item in self.__dict__.items()]))
x = Vip("AAA")
x.get_info()
