class Student():
    def __init__(self,id = "0",name = "qqq",courses = ["sdasd"]):
        self.id = id
        self.name = name
        self.courses = courses
    def __str__(self):
        return "学生id "+self.id+"\n学生名字 "+self.name+"\n学生课程 "+str(self.courses)
    def __del__(self):
        print("Student has been deleted")
    def add_course(self,adsada):
        self.courses.append(adsada)
    def del_course(self,which):
        self.courses.pop(which)
class Course ():
    def __init__(self,id = "0",name = "qqq",students = ["sdasd"]):
        self.id = id
        self.name = name
        self.students = students
    def del_course(self,id):
        self.students.pop(id)
    def add_course(self,adsada):
        self.students.append(adsada)