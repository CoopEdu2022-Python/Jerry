from user import User


class Student(User):
    id = "uid_student"

    def __init__(self, point: int):
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
