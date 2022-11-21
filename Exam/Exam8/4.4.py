# 4.4.1  基础版  [20pts]
# 1. 定义玩家类 Player，包含属性 points；方法 punch()，随机返回 '10'，'5'，'2'
# 2. 定义电脑类 Computer，继承自 Player
# 3. 定义函数 game()：玩家和电脑分别出拳（1 次），胜利方得 1 分；打印并返回结果
# 4.4.2  骗子版  [20pts]
# 1. 添加骗子类 Fraud，包含方法 lie()，随机返回 'lose'，'tie'
# 2. 为 Player 类添加方法 challenge()，随机返回 'yes'，'no'
# 3. 修改 game()：玩家和电脑出拳后，玩家需要询问骗子结果，如果玩家不挑战，则按照骗子的结果进行计分；如果玩家挑战，则按照真实情况计分，但是分值 * 2
# 例1：玩家胜利，骗子告知 'lose'，如果玩家挑战（返回 'yes'），则获得 2 分
# 例2：玩家失败，骗子告知 'lose'，如果玩家挑战，则电脑获得 2 分
# 例3：玩家胜利，骗子告知 'tie'，如果玩家不挑战，则无事发生
import random
class Player():
    def __init__(self):
        self.points = 0
    def punch(self):
        return random.choice(['10','5','2'])
class Computer(Player):
    pass
def game():

    if player.punch() == 10 and computer.punch() == 5:
        computer.points += 1
    if player.punch() == 5 and computer.punch() == 2:
        computer.points += 1
    if player.punch() == 2 and computer.punch() == 5:
        computer.points += 1
    if computer.punch() == 2 and player.punch() == 5:
        player.points += 1
    if computer.punch() == 5 and player.punch() == 2:
        player.points += 1
    if computer.punch() == 10 and player.punch() == 5:
        player.points += 1
player = Player()
computer = Computer()
for _ in range(10):
    game()
print(computer.points,player.points)