# 4.3.5 改写 #4.2.5：函数内不打印菱形，将需要打印的菱形作为函数的返回值，用 2 种方式调用函数，传入不同的参数，打印 2 个不同的菱形
def lingxing(hight):
    sames = str("")
    sames_1 = str("")
    if hight % 2 == 0:
        print("别输入偶数啊Σ(っ °Д °;)っ")
    else:
        a = 1
        for i in range(1, hight + 1, 2):
            a = a + 1
            x = str(" " * (hight - a)+"*" * i)
            sames = sames + "\n" + x
            continue
        for i in range(hight - 2, 0, -2):
            a = a - 1
            y = str(" " * (hight - a)+"*" * i)
            sames_1 = sames_1 + "\n"+ y
            continue
        return sames+sames_1

print(lingxing(int(input("输入高度"))))

#不知道咋搞