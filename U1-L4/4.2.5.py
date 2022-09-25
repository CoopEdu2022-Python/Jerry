# 4.2.5 参考上节课练习 #3.3.2 的打印菱形，定义一个函数，能够根据不同的参数打印不同大小的菱形
def lingxing(hight):
    if hight % 2 == 0:
        print("别输入偶数啊Σ(っ °Д °;)っ")
    else:
        a = 1
        for i in range(1, hight + 1, 2):
            a = a + 1
            print(" " * (hight - a), end="", sep="")
            print("*" * i)
        for i in range(hight - 2, 0, -2):
            a = a - 1
            print(" " * (hight - a), end="", sep="")
            print("*" * i)
lingxing(int(input("输入高度")))