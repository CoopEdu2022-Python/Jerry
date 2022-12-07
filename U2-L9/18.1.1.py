class A():
    nums = 0
    def __init__(self):
        self.nums = 0
    @staticmethod
    def test1():
        return [name for name in dir(A) if name[:2]!="__"and name [::-1][:2] != "__"]
    @classmethod
    def test2(cls):
        return [name for name in dir(cls) if name[:2] != "__" and name[::-1][:2] != "__"]
    def test3(self):
        return [name for name in dir(self) if name[:2] != "__" and name[::-1][:2] != "__"]
a = A()
print(A.test1())
print(A.test2())
print(a.test3())
