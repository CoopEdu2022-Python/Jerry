import random
class FIsh():
    def __init__(self):
        self.x = random.randint(0,10)
        self.y = random.randint(0, 10)
        self.speed = 1
    def move(self):
        if random.randint(0,1) == 0:
            self.x += random.randint(-1,1)


    pass
class Bigfish(FIsh):
    def __init__(self):
        super().__init__()
        self.Hp = 100
    def move(self):
        pass
    pass
    def eat(self):
        self.Hp +=20

class Smallfish(FIsh):
    pass
