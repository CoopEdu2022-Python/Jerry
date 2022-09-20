# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
i = 1
x = int(input("shu"))
while i < 1000:
    i = i+1
    if x % i == 0:
        print(i)
        if x == i:
            print("无")
        else:

            x = x / i
#bug 在计算结果出现同一数字时有错 40可以 27不行