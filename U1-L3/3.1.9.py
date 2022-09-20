# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
a = int(input(("输入一个数字\n")))
for i in (2 , a , 1):
    if a % i == 0:
        if i == a:
            print("质数")
            break
        elif i != a:
            print("合数")
            break

    else:
        i = i+1
