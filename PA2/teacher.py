import os
from user import User
import students


class Teacher(User):
    def __init__(self, account_number: str, password: str, name: str):
        super().__init__(name, account_number, password)
        self.jurisdiction = "teacher"

    def __add_students(self):
        student_name = str(input("输入想要添加的姓名"))
        student_account = str(input("输入初始账号"))
        while 1:
            if find_account(student_account):
                print("该用户已存在")
                student_account = input("请重新输入初始账号:")
            else:
                break
        add_student(student_account, student_name)
        print("创建成功")
    @staticmethod
    def add_course():
        x = str(input("输入创建课程名"))
        if judge_course_existence(x) is not False:
            return "该课程已存在"
        c = input("选修or必修")
        imformation = [str(x), [], c]
        full_name = "course_data/" + x + ".txt"
        file = open(full_name, mode="w")
        file.write(str(imformation))
        file.close()
        return "已完成"
    @staticmethod
    def read_coursedata():
        ke = input("请输入课程名")
        print(os.listdir('course_data'))
        print(judge_course_existence(ke))
    def user_board(self):
        while 1:
            click = str(input("可输入'用户身份','课程信息','学分要求','创建课程','创建学生','查询学生','登出'"))
            if click == "登出":
                return "break"
            elif click == "创建学生":
                return self.__add_students()
            elif click == "创建课程":
                print("行！￣へ￣")
                return self.add_course()
            elif click == "课程信息":
                print("中！<(￣︶￣)↗[GO!]")
                return self.read_coursedata()
            if click not in['用户身份','课程信息','学分要求','创建课程','查询学生','登出']:
                break

            boardlist = { "用户身份": self.name}
            return boardlist[str(click)]


def judge_course_existence(name):
    for _ in range(len(os.listdir('course_data'))):
        if str(name) + ".txt" == os.listdir("course_data")[_]:
            return os.listdir("course_data")[_]
    print("A")
    return False


def find_account(account):
    for _ in range(len(os.listdir('students'))):
        if str(account) + ".txt" == os.listdir("students")[_]:
            return True
    return False


def add_student(account, name):
    account = str(account)
    imformation = "students/", "123456", str(name), "student", ["no class"], ""
    full_name = "students/" + account + ".txt"
    file = open(full_name, mode="w")
    file.write(str(imformation))
    file.close()
    return
