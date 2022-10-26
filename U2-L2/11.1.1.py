class Student:
    def __init__(self):
        self.courses = []
        self.id = input("ID")
        self.name = input("name")

    def __del__(self):
        print("已删除学生：[%s][%s]" % (self.name,self.id))

    def add_courses(self):
        while 1:
            class_choose = input("请输入课程")
            self.courses.append(class_choose)
            judge = input("还有课程吗？(Y/N)")
            if judge == "Y":
                continue
            elif judge == "N":
                return self.courses


    def get_course(self):
        print(self.courses)
    def __len__(self):
        return len(self.courses)
student1 = Student()
student1.add_courses()
print(student1.name)
print(student1.courses)
print(len(student1.courses))
del student1
