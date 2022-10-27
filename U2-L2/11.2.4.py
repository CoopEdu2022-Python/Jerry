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
student_1 = Student('xxs', '9')

for day in range(30):
    student_1.study()

print(student_1.score, student_1.mood)

for day in range(31, 0, -1):
    student_1.play()

print(student_1.score, student_1.mood)

if student_1.score < 70:
    del student_1