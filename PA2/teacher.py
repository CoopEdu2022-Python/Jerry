import os
from user import User
class Teacher(User):
    def __init__(self, account_number: str, password: str, name: str):
        super().__init__(name, account_number, password)
        self.jurisdiction = "teacher"
    def add_students(self):
        student_name = str(input("输入想要添加的姓名"))
        student_account = str(input("输入初始账号"))
        while 1:
            if find_account(student_account):
                print("该用户已存在")
                student_account = input("请重新输入初始账号:")
            else:
                break
        add_student(student_account,student_name)
        print("创建成功")
    def user_board(self):
        while 1:
            click = input("可输入'用户身份','课程信息','学分要求','创建课程','创建学生','查询学生','登出'")
            if click == "登出":
                break
            else:
                boardlist = {"用户身份": self.name, '创建学生':self.add_students()}
                return boardlist[click]


def find_account(account):
    for _ in range(len(os.listdir('students'))):
        if str(account)+".txt"  == os.listdir("students")[_]:
            return True
    return False
def add_student(account, name):
    account = str(account)
    print(os.listdir('students'))
    global student_way
    student_way = "students/"
    imformation = str(account), "123456", str(name), "student",["no class"],""
    full_name = student_way + account + ".txt"
    file = open(full_name, mode="w")
    file.write(str(imformation))
    file.close()
    return
