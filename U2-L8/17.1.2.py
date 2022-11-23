class Fruit():
    type_number = 0

    @staticmethod
    def variety():
        return Fruit.type_number


class A():
    def __init__(self):
        Fruit.type_number += 1

    def __del__(self):
        Fruit.type_number -= 1


class B():
    def __init__(self):
        Fruit.type_number += 1

    def __del__(self):
        Fruit.type_number -= 1


class C():
    def __init__(self):
        Fruit.type_number += 1

    def __del__(self):
        Fruit.type_number -= 1


class D():
    def __init__(self):
        Fruit.type_number += 1

    def __del__(self):
        Fruit.type_number -= 1


class E():
    def __init__(self):
        Fruit.type_number += 1

    def __del__(self):
        Fruit.type_number -= 1


a = A()
b = B()
f = Fruit()
print(f.variety())
del b

print(f.variety())
