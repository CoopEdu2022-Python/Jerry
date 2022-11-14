class Animal:
    def __init__(self,health):
        self.health = health
class Manager:
    def __init__(self):
        self.__performance = 100
    def feed(self, animal):
        animal.health += 20
        return animal.health
    def perform(self, animal):
        animal.health -= 20
        return animal.health
    def __inspect(self,person):
        return person.__performance
    def open_inspenct(self,person):
        self.__inspect(self)
class Keeper(Manager):
    def __init__(self):
        super()
        self.performance = 100
    def ctrl_perfor(self,animal):
        if animal.health < 80:
            self.performance -= 20
        return self.performance
class Trainer(Manager):
    def feed(self, animal):
        pass

class everyday():
    animal = Animal(100)
    manager = Manager()
    keeper = Keeper()
    trainer = Trainer
    keeper.ctrl_perfor(animal)
    keeper.feed(animal)
    keeper.perform(animal)
    manager.open_inspenct(trainer)
    manager.open_inspenct(keeper)








