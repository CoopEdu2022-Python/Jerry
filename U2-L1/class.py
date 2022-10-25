class Student:  # Student 是类
    def study(self):  # 实例方法
        print('sleeping')


student_1 = Student()  # 创建了一个 student_1 是对象

student_1.name = 'Jane Doe'  # 为 student_1 新建属性
student_1.age = 16
student_1.score = 'F'

print(dir(Student))
print(dir(student_1))

student_1.study()