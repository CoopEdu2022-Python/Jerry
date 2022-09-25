# 4.2.6 参考上节课练习 #3.3.3 的打印乘法表，定义一个函数，能够根据不同的参数，打印不同范围的九九乘法表，例如参数为 1 时，
# 只打印 '1 * 1 = 1'；参数为 9 时，打印完整的内容
def chengfakoujue(c):
    for a in range(1, c+1, 1):
        print("\n")
        for b in range(1, a+1, 1):
            if b == 10:
                break
            else:
                print("%d" % (a), "*", "%d" % (b), "=", "%d" % (a * b), end="    ")
chengfakoujue(int(input("1~9: ")))