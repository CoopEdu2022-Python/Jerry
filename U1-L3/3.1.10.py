# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
i = 2
x = int(input("shu"))
while i < 1000:
    if x % i == 0:
        print(i)
        if x == i:
            break

        elif x != i:

            x = x / i
            continue
    i = i + 1
