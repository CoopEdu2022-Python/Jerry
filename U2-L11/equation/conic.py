class Ellipse:
    pass


class Circle(Ellipse):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def area(self, r):
        return 3.14 * (self.r ** 2)
