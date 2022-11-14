class Animal:
    def __init__(self,health):
        health = int(health)
class Manager:
    def __init__(self,jixiao):
        self.__jixiao = jixiao
    def feed(self, animal):
        animal.health += 20
        return animal.health
    def perform(self, animal):
        animal.health -= 20
        return animal.health
    def __inspect(self):
        return self.jixiao


