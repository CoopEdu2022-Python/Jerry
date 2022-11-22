# 1. 类方法如何定义？
class A():
    @classmethod
    def AAA(cls):
        pass
# 2. 静态方法如何定义？
class B():
    @staticmethod
    def BBB():
        print("BBB")
B.BBB()