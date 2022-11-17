import random


class Dealer():
    def __init__(self):
        self.__munber = int()
        self.rounds = 0

    def set_number(self):
        self.__munber = random.randrange(0, 100, 1)

    def hint(self, n):

        self.rounds += 1
        if n == self.__munber:
            print("猜对了")
            return True
        elif n > self.__munber:
            print("猜大了")
            return False
        else:
            print("猜小了")
            return False

    def hint2(self, n):

        if n == self.__munber:
            return "猜对了"
        elif n > self.__munber:
            return "猜大了"
        else:
            return "猜小了"

    def award(self):
        return 20 - self.rounds


class Player():
    def __init__(self):
        self.point = 0
        self.n1 = 0
        self.n2 = 100

    def guess_number(self, n1 = 0, n2 = 100):
        x = random.randrange(n1, n2, 1)
        if dealer.hint2(x) == "猜对了":
            return x
        elif dealer.hint2(x) == "猜大了":
            self.n2 = x - 1
        elif dealer.hint2(x) == "猜小了":
            self.n1 = x + 1
        return x
def game():
    dealer.set_number()
    dealer.hint(player.guess_number())

class Rule():
    def __init__(self):
        self.rounds = 0
    def add(self):
        self.rounds += 1
    def judge(self, player:Player, dealer:Dealer):
        player.point = dealer.award()

dealer = Dealer()

player = Player()

rule = Rule()

while 1:
    if dealer.award() > -10 and dealer.hint(player.guess_number()) == False:
        game()
    else:
        break
rule.judge(player,dealer)
print(player.point)