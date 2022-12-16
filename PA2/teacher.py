from user import User
class Teacher(User):
    def __init__(self, name: str, account_number: str, password: str):
        super().__init__(name, account_number, password)
        self.jurisdiction = "teacher"
    def add_student(self):
        student_name = input("输入想要添加的姓名")
        student_account = input("输入初始账号")
    def user_board(self):
        while 1:
            click = input("可输入'用户身份','课程信息','学分要求','登出'")
            if click == "登出":
                break
            else:
                boardlist = {"用户身份": self.name, "课程信息": self.course}
                return boardlist[click]
