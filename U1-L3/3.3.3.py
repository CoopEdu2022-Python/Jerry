# 3.3.3 按照下列格式打印九九乘法表
'''
1 * 1 = 1
1 * 2 = 2    2 * 2 = 4
1 * 3 = 3    2 * 3 = 6    3 * 3 = 9
……
'''
for a in range(1,10,1):
    print("\n")
    for b in  range(1,10,1):
        if b == 10:
            break
        else:
            print("%d"% (a), "*", "%d"% (b), "=","%d" % (a*b),end="    ")