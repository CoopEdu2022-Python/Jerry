from user import User
import os

class Student(User):
    id = "uid_student"

    def __init__(self, account_number: str, password: str, name: str, id_, course:list):

        super().__init__(account_number, password, name)

        self.course = course
        self.__password = password
        self.id_ = id_
        self.account = account_number
        self.name = name

    def chack_class(self):

        x = str(input("查看课程"))
        for _ in range(len(os.listdir("course_data"))):
            if str(x)+".txt"  == os.listdir("course_data")[_]:
                filer = open("course_data/"+os.listdir("course_data")[_],mode="r")
                linesread = filer.readlines()
                filer.close()
                print(linesread[0].split(",")[0],linesread[0].split(",")[2])
                return (linesread[0])

            else:
                continue
        print("未查询该课程")
    def get_self(self):
        return self.name
    def user_board(self):
        while 1:
            click = input("可输入'用户身份','课程信息','学分要求','登出','加入课程'")
            if click == "登出":
                return "break"
            else:
                boardlist = {"用户身份": self.get_self(), "课程信息": self.course,"加入课程":self.chack_class()}
                return boardlist[click]

    def identity(self):
        return self.id_

    def find_course(self):
        return self.course

    def get_course(self, course_name):
        # if 成功
        self.course.append(course_name)

        return self.name, course_name
    def test(self):
        print(self.account)
        print(self.__password)

    def drop_course(self, course_name):
        # if 成功
        self.course.pop(course_name)
        return self.name, course_name


