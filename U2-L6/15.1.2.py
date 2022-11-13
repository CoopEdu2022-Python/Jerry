import random
class FIsh:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        if random.randint(0, 1):
            self.x += random.randint(-1, 1)
            self.x = self.set_real(self.x)
        else:
            self.y += random.randint(-1, 1)
            self.y = self.set_real(self.y)
        print(self.x, self.y)
        return (self.x,self.y)

    def set_real(self, o):
        if o > 10:
            return 9
        if o < 0:
            return 1
        return o


    pass
class Smallfish(FIsh):
    def __del__(self):
        print(
            "被吃了"
        )
    def being_eat(self):

    pass
class Bigfish(FIsh):
    def __init__(self):
        super().__init__()
        self.Hp = 100
    def move(self):
        if random.randint(0, 1):
            self.x += random.randint(-1, 1)
            self.x = self.set_real(self.x)
        else:
            self.y += random.randint(-1, 1)
            self.y = self.set_real(self.y)
        self.Hp -= self.Hp
        print(self.x, self.y)
        return (self.x,self.y)
    def eat(self):
        if self.move() == Smallfish.move():
            for number in range (Smallfish.numbers,0,-1):
                self.Hp +=20

