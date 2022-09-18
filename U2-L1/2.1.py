# 2.1.1 外星人颜色
# 请创建一个名为 alien_color 的变量，并将其设置为 'green'、'yellow' 或 'red'
# 编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了 5 个 points
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）
alien_color = "red"
if alien_color == "green" :
    print("get five points")

alien_color_1 = "green"
if alien_color_1 == "green" :
    print("get five points")
# 2.1.2 像 #2.1.1 那样设置外星人的颜色，并编写一个 if-else 结构
# 如果外星人不是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个 points
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 10 个 points
# 编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块
if alien_color == "green":
    print("get ten points")
else:
    print("get five points")

if alien_color_1 == "green":
    print("get ten points")
else:
    print("get five points")
# 2.1.3 将 #2.1.2 中的 if-else 结构改为 if-elif-else 结构
# 如果外星人是红色的，就打印一条消息，指出玩家获得了 5 个 points
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 10 个 points
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了 15 个 points
# 编写这个程序的三个版本，它们分别在外星人为红色、绿色和黄色时打印一条消息
alien_color_2 = "yellow"
if alien_color_1 == "green":
    print("get ten points")
elif alien_color_1 == "red":
    print("get five points")
elif alien_color_1 == "yellow":
    print("get fifteen points")

if alien_color == "green":
    print("get ten points")
elif alien_color == "red":
    print("get five points")
elif alien_color == "yellow":
    print("get fifteen points")

if alien_color_2 == "green":
    print("get ten points")
elif alien_color_2 == "red":
    print("get five points")
elif alien_color_2 == "yellow":
    print("get fifteen points")
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
#2.1.5 学生输入一个成绩，对不同的成绩进行评价（标准自定）
student_grade = int(input("请输入成绩\n"))
if student_grade >= 60:
    print("合格啦！")
else:
    print("那你死定了q(≧▽≦q)")