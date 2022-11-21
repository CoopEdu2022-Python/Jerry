import random
class Player():
    def __init__(self):
        self.points = 0
    def punch(self):
        return random.choice([10,5,2])
    def challenge(self):
        return random.choice(["yes", "no"])
class Computer(Player):
    pass

class Fraud:
    def lie(self):
        return random.choice(["lose", "tie"])
def add_point(numbers):
    if player.punch() == 10 and computer.punch() == 5:
        computer.points += numbers
    if player.punch() == 5 and computer.punch() == 2:
        computer.points += numbers
    if player.punch() == 2 and computer.punch() == 5:
        computer.points += numbers
    if computer.punch() == 2 and player.punch() == 5:
        player.points += numbers
    if computer.punch() == 5 and player.punch() == 2:
        player.points += numbers
    if computer.punch() == 10 and player.punch() == 5:
        player.points += numbers
def game():
    if player.challenge() == "yes":
        add_point(2)
    else:
        if fraud.lie() == "lose":
            computer.points += 1
        else:
            return
fraud = Fraud()
player = Player()
computer = Computer()
for _ in range(10):
    game()
print(computer.points,player.points)
