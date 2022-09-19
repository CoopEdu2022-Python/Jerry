# 3.1.5 猜数游戏 v2.1
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，用户可以一直猜，直到猜对为止
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，告知误差范围：如果误差超过 50，打印 '离谱'；误差超过 30，打印 'nonono'；误差不超过 10，打印 'close!'
import random
r = random.randint(1,100)
i = 0
while 5 >+ i:
    answer = int(input("在100到1之间猜数字，还剩余" "%d" "次机会哦\n" %(5-i)))
    if answer == r:
        print("恭喜你答对啦！")
        break
    elif answer < r:
        print("猜小了")
        if abs(r - answer) < 10:
            print("close")
        elif abs(r - answer) >= 10 and  abs(r - answer) < 30:
            print("nonono")
        elif abs(r - answer) >= 30 and  abs(r - answer) < 50:
            print("离谱")

    elif answer > r :
        if abs(r - answer) < 10:
            print("close")
        elif abs(r - answer) >= 10 and  abs(r - answer) < 30:
            print("nonono")
        elif abs(r - answer) >= 30 and  abs(r - answer) < 50:
            print("离谱")
        print("猜大了")

    i = i+1