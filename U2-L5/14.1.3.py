# Point 类包含 2 个属性，分别为点的横坐标与纵坐标
# Segment 类包含 2 个私有属性，分别为两个端点的坐标
# Segment 类包含 get_len() 方法，可以获得直线的长度
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x,self.y)

class Segment():
    def __init__(self,x, y, ex, ey):



    def get_len(self):
        return math.sqrt(abs() ** 2 + abs() ** 2)