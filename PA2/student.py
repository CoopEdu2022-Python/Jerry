from user import User


class Student(User):
    id = "uid_student"

    def __init__(self, point: int, name: str, account_number: str, password: str):
        super().__init__(name, account_number, password)
        self.point = point
        self.course = []
        self.jurisdiction = "student"

    def identity(self):
        return self.jurisdiction

    def get_course(self, course_name):
        # if 成功
        self.course.append(course_name)

        return self.name, course_name

    def drop_course(self, course_name):
        # if 成功
        self.course.pop(course_name)
        return self.name, course_name

    def add_student(self):
        student_name = input("输入想要添加的姓名")
        student_account = input("输入初始账号")