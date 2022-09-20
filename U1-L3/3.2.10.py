# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
a = int(input(("输入一个数字\n")))


for i in (1 , a , 1):
    if a % i ==0:
        if i == a:
            print(i)
            break
        elif i != a:
            print(i)
            a = a/i


    else:
        i = i+1

#bug 在计算结果出现同一数字时有错 40可以 27不行