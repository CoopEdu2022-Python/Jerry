def lingxing(hight):
    if hight % 2 == 0:
        print("别输入偶数啊Σ(っ °Д °;)っ")
    else:
        a = 1
        for i in range(1, hight + 1, 2):
            a = a + 1
            print(" " * (hight - a)+"*" * i, sep="")

        for i in range(hight - 2, 0, -2):
            a = a - 1
            print(" " * (hight - a)+"*" * i, sep="")

lingxing(int(input("输入高度")))
#不知道咋搞