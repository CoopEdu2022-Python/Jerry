class Student:
    def __init__(self):
        self.courses = []
        self.id = input("ID")
        self.name = input("name")
        while 1:
            class_choose = input("请输入课程")
            self.courses.append(class_choose)
            while 1:
                judge = input("还有课程吗？(Y/N)")
                if judge == "Y":
                    break
                elif judge == "N":
                    return
                else:
                    continue

    def __del__(self):
        print("已删除学生：[%s][%s]" % (self.name, self.id))

    def get_course(self):
        print(self.courses)
    def __len__(self):
        return len(self.courses)
student1 = Student()

print(student1.name)
print(student1.courses)
print(len(student1.courses))
del student1
