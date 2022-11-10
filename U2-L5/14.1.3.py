# Point 类包含 2 个属性，分别为点的横坐标与纵坐标
# Segment 类包含 2 个私有属性，分别为两个端点的坐标
# Segment 类包含 get_len() 方法，可以获得直线的长度
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment(Point):
    def __init__(self,x, y, px, py):
        self.x = x
        self.y = y

        self.__x = px
        self.__y = py

    def get_len(self):
        return math.sqrt(abs(self.__x.x - self.__y.x) ** 2 + abs(self.__y.x - self.__x.x) ** 2)