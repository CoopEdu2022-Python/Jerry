# 2.1.3 将 #2.1.2 中的 if-else 结构改为 if-elif-else 结构
# 如果外星人是红色的，就打印一条消息，指出玩家获得了 5 个 points
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 10 个 points
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了 15 个 points
# 编写这个程序的三个版本，它们分别在外星人为红色、绿色和黄色时打印一条消息
alien_color = "red"
alien_color_1 = "green"
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