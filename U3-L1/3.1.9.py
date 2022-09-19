# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
start_number = 2
x_r = int(input(""))
while start_number % x_r == 0:

    if x_r == start_number:
        print("质数")
        break

    start_number = start_number + 1