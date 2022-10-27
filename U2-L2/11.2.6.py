class Student:
    def __init__(self, name=None, student_id='0'):
        self.name = name
        self.student_id = student_id
        self.score = 70
        print('{} enrolled! (id: {})'.format(name, student_id))

    def __del__(self):
        print('{} dropped out! (id: {})'.format(self.name, self.student_id))

    def __str__(self):
        info = 'name: {}\nid: {} '.format(self.name, self.student_id)
        return info

    def study(self):
        self.score += 1
        self.mood = 'good'

    def play(self, days=1):
        if self.score < 70 or self.score > 90:
            self.mood = 'perfect'
        else:
            self.mood = 'bad'
        self.score -= (days - 1)

    def self_introduction(self):
        print(self)


# main program writes below
# ...
# ..
student_1 = Student()
student_2 = Student()

student_1.study()
len_1 = len(dir(student_1))  # dir 返回对象的所有属性 + 方法的列表
len_2 = len(dir(student_2))
print(len_1 - len_2)