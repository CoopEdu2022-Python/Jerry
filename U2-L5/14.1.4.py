class A:
    def test(self):
        print(1)


class B(A):
    def test(self):
        print(2)


class C(B):
    def test(self):
        A.test(self)
    pass
c = C()
c.test()