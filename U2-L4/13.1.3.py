class A:
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.Z = 3

    def get_X(self):
        print(self.X)


class B(A):
    def get_Y(self):
        print(self.Y)


class C(B):
    def get_Z(self):
        print(self.Z)


a = A()# get_X和属性
b = B()# get_X get_Y 属性
c = C()# get_X get_Y get_Z 属性