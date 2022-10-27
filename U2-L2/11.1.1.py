class Student:
    def __init__(self,name = str(),id = str()):
        self.courses = []
        self.id = id
        self.name = name
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
    def __str__(self):
        return "name: {}\n  id:{}".format(self.name, self.id)
    def __del__(self):
        print("已删除学生：[%s][%s]" % (self.name, self.id))

    def get_course(self):
        print(self.courses)
    def __len__(self):
        return len(self.courses)
student1 = Student("a","0")

print(student1)
print(student1.courses)
print(len(student1.courses))
del student1
