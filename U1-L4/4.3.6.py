# 4.3.6 改写 #4.2.6：函数内打印乘法表，同时，将打印的算式条数作为函数的返回值。例如完整的乘法表，应有 9+8+7+……+1 共 45 条算式。用任意的方式调用函数，打印乘法表的同时，在下方打印算式条数
# 只打印 '1 * 1 = 1'；参数为 9 时，打印完整的内容
def chengfakoujue(c):
    x = 0
    for a in range(1, c+1, 1):
        for b in range(1, a+1, 1):
            if b == 10:
                break
            else:
                x = x+1
    return x
print(chengfakoujue(int(input("1~9: "))))