import random


class Dealer():
    def __init__(self):
        self.__munber = None
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

    def award(self):
        return 20 - self.rounds


class Player():
    def __init__(self):
        self.point = 0

    def guess_number(self):
        return random.randrange(0, 100, 1)
def game():
    dealer.set_number()
    dealer.hint(player.guess_number())


dealer = Dealer()
player = Player()
game()

