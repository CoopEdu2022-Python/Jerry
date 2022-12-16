from user import User


class Student(User):
    id = "uid_student"

    def __init__(self, account_number: str, password: str, name: str, id_, course:list):

        super().__init__(account_number, password, name)

        self.course = course
        self.__password = password
        self.id_ = id_
        self.account = account_number
        self.name = name
    def get_self(self):
        return self.name
    def user_board(self):
        while 1:
            click = input("可输入'用户身份','课程信息','学分要求','登出'")
            if click == "登出":
                break
            else:
                boardlist = {"用户身份": self.get_self(), "课程信息": self.course}
                print(boardlist[click])

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


a = Student("1","2","3","4",[])
a.test()