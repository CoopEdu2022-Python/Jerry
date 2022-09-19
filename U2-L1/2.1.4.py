# 2.1.4 猜数游戏
# 在程序中设定一个 1-100 的数
# 让用户输入一个数
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，告知用户正确答案，并显示 “猜大了” 或 “猜小了”

import random
r = random.randint(1,100)
i = 1
while 6 >= i:
    answer = int(input("猜数字100到1之间还剩余" "%d" "次机会哦\n" %(7-i)))
    if answer == r:
        print("恭喜你答对啦！")
        break
    elif answer < r:
        print("小了")
    elif answer > r :
        print("大了")


    i = i+1


print("答案为%r" % r)