# Exam 类包含4实例属性: id, start_time, end_time, pointsTest类继承自Exam类,不同的是, Test类不包含起始和终止时间,points属性永远为10
class Exam:
    def __init__(self,id,start_time,end_time,points):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.points = points

class Test(Exam):
    def __init__(self):
        self.id = ""
        self.points = 10
class Ather(Exam):
    def __init__(self):
        super()
B = Exam("123","321","1234","4321")
A = Test()
print('\n'.join(['{0}: {1}'.format(item[0], item[1]) for item in B.__dict__.items()]))

print('\n'.join(['{0}: {1}'.format(item[0], item[1]) for item in A.__dict__.items()]))
