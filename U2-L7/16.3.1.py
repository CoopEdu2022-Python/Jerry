import random
safe = []
class Player():
    def __init__(self,number):
        self.__number = number
    def __del__(self):
        print("%s号被杀",self.__number)
class Goodpeaple():
    pass

class Mafia(Player):
    def __init__(self,*safe:list):
        self.safe = list(safe)
    def kill(sele,list_alive):
        sele.safe.remove((random.randint(0,len(list_alive))))

class Judge():


    def initialize(self):
        x = 0
        while x < 3:
            safe = []
            x = 0
            for _ in range(1,10):
                if random.randint(0,1) == 1 or x >= 3:
                    safe.append(Goodpeaple().__init__(_))
                else:
                    safe.append(Mafia().__init__(_))
                    x += 1
        return safe
    def play(self):
        print("night coming")
        Mafia.kill()
        print("day")




judge = Judge

judge.initialize()
while Goodpeaple not in safe:
    judge.play()


