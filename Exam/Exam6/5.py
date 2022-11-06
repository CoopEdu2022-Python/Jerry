class Course:
    def __init__(self, name="", time=0):
        self.name = name
        self.time = time
    def __str__(self):
        return  ("Class " + self.name +" spend " + str(self.time))
    def get_name(self):
        return self.name
    def get_time(self):
        return self.time
print(Course("Math",60))