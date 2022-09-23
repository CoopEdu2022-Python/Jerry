# 3.1.4 猜数游戏 v2.0
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，最多有 5 次机会
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，显示 “猜大了” 或 “猜小了”
import random
r = random.randint(1,100)
i = 0
while 5 > i:
    answer = int(input("在100到1之间猜数字，还剩余" "%d" "次机会哦\n" %(5-i)))
    if answer == r:
        print("恭喜你答对啦！")
        break
    elif answer < r:
        print("猜小了")
    elif answer > r :
        print("猜大了")

    i = i+1