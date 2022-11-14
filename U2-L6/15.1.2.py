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



    def set_real(self, o):
        if o > 10:
            return 9
        if o < 0:
            return 1
        return o


    pass
class Smallfish(FIsh):
    def move(self):
        super(Smallfish, self)
        print("小鱼在 (%d , %d)"% (self.x,self.y))
        return(self.x,self.y)
    def being_eat(self):
        print("被吃了__________________")
    def give_location(self):
        return (self.x, self.y)

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
        self.Hp -= 1
        print("大鱼在 (%d , %d)"% (self.x,self.y))
        print("大鱼Hp %d"% self.Hp)
        return (self.x,self.y)
    def eat(self):
        self.Hp += 20
x = []
bigfish = Bigfish()
for _ in range(10):
    x.append(Smallfish())
while x != [] and bigfish.Hp >= 1:
    safe = bigfish.move()
    for a in x:
       a.move()
    i = 0
    while i <= len(x)-1:
        if x[i].give_location() == safe:
            bigfish.eat()
            x[i].being_eat()
            x.pop(i)
        else:

            i += 1

print("game over")