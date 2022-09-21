# 3.3.4 用户输入 1 个整数，打印出这个整数的所有因数。打印后程序持续运行，而非结束
while 1:
    i = 2
    x = int(input("输入数字开始因式分解 \n"))
    while i < 1000:
        if x % i == 0:
            print(i)
            if x == i:
                break

            elif x != i:

                x = x / i
                continue
        i = i + 1
