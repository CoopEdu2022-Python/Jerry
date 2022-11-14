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
    def __del__(self):
        print("被吃了")
    def being_eat(self):
        del self

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
        print("大鱼在 (%d , %d)"% (self.x,self.y))
        return (self.x,self.y)
    def eat(self):
        self.Hp += 20
x = []
bigfish = Bigfish()
for _ in range(11):
    x.append(Smallfish())
while x != [] or bigfish.Hp != 0:
    bigfish.move()
    for a in range(10):
       x[a].move()
    i = 0
    while i <= 10:
        if x[i].move() == bigfish.move():
            bigfish.eat()
            x[i].being_eat()
            x.pop(i)
        else:
            i += i
            break
print(x)