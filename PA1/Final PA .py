import os

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 将列表打印为图像
def checkerboard_print(safe_list):
    safe_list = list(safe_list)
    if not win(safe_list):
        os.system("cls")
        for _ in range(0, 3):

            for i in range(0, 3):
                print("| ", " ", end="|", sep="%s" % str(safe_list[int(3 * _ + i)]))
            if _ == 2:
                break
            else:
                print("\n", "——--——--——--——-", sep="")

    else:
        os.system("cls")
        for _ in range(0, 3):
            for i in range(0, 3):
                print("| ", " ", end="|", sep="%s" % str(safe_list[int(3 * _ + i)]))
            if _ == 2:
                break
            else:
                print("\n", "——--——--——--——-", sep="")
        print("\n", "游戏结束了")
        return


def who_get_chess(safe_player):
    while 1:
        if safe_player % 2 == 1:
            print("\n", "由 x 执棋", end="")
        elif safe_player % 2 == 0:
            print("\n", "由 o 执棋", end="")
        return


# 输入输出棋子数量——操作
# 同时也是普通玩法，加上防呆
def judge_checkerboard(safe_list):
    safe_player = 0
    _ = 0
    while 1:

        while 1:
            who_get_chess(safe_player)
            location = input("下在哪里'输入数字1~9'")
            if str(location).isalpha():
                print("不可以输入字母")
                continue
            elif str(location) == "":
                print("请勿输入空")
                continue
            elif not str(location).isalnum():
                print("!!!输入数字1~9!!!")
                continue
            elif 1 > int(location) or 9 < int(location):
                print("超出范围!!!输入数字1~9!!!")
                continue
            elif safe_list[int(location) - 1] == "o" or safe_list[int(location) - 1] == "x":
                print("该位置已经有一个棋子了")
                continue
            else:
                safe_player = int(safe_player) + 1
                break
        if str(location) == str(safe_list[int(location) - 1]):
            if _ % 2 == 1:
                safe_list[int(location) - 1] = "x"
            else:
                safe_list[int(location) - 1] = "o"
        checkerboard_print(safe_list)
        _ += 1
        if win(safe_list) == "1000":
            print(str("%s子赢了" % (safe_list[int(location) - 1])))
            return
        elif win(safe_list) == "5050":
            print("平局")
            return
        else:
            continue
    if win(safe_list) == "1000" or win(safe_list) == "5050":
        return


# 判断输赢。由于有一盘棋有三种结局所以True和False会重合所以用数字表示。5050平局1000一方胜利
def win(safe_list):
    safe_list = list(safe_list)
    if 1 in safe_list or 2 in safe_list or 3 in safe_list or 4 in safe_list or 5 in safe_list or \
            6 in safe_list or 8 in safe_list or 9 in safe_list:
        if safe_list[0] == safe_list[1] == safe_list[2] or safe_list[2] == safe_list[5] == safe_list[8] or \
                safe_list[6] == safe_list[7] == safe_list[8] or safe_list[0] == safe_list[3] == safe_list[6] or \
                safe_list[6] == safe_list[4] == safe_list[2] or safe_list[8] == safe_list[4] == safe_list[0] or \
                safe_list[3] == safe_list[4] == safe_list[5] or safe_list[7] == safe_list[4] == safe_list[1]:
            return "1000"
        else:
            return False
    else:
        return "5050"


# 变化玩法。这一段比较长但是仔细看能发现其实大多数都是防呆。如果时间充裕可把这部分独立出来封装函数。
def after_6times_gaming(safe_list):
    safe_chessGoing = []
    safe_player = 0
    list_record = []
    for _ in range(0, 6):
        while 1:
            who_get_chess(safe_player)
            location = input("下在哪里'输入数字1~9'")
            if str(location).isalpha():
                print("不可以输入字母")
                continue
            elif str(location) == "":
                print("请勿输入空")
                continue
            elif not str(location).isalnum():
                print("!!!输入数字1~9!!!")
                continue
            elif 1 > int(location) or 9 < int(location):
                print("超出范围!!!输入数字1~9!!!")
            elif safe_list[int(location) - 1] == "o" or safe_list[int(location) - 1] == "x":
                print("该位置已经有一个棋子了")
                continue


            else:
                safe_player = int(safe_player) + 1
                break
        if str(location) == str(safe_list[int(location) - 1]):
            safe_chessGoing.append(str(location))
            if _ % 2 == 1:
                safe_list[int(location) - 1] = "x"
            else:
                safe_list[int(location) - 1] = "o"
        checkerboard_print(safe_list)
        list_record.append(int(location))
        if win(safe_list) == "1000":
            print(str("%s子赢了" % (safe_list[int(location) - 1])))
            return
        elif win(safe_list) == "5050":
            print("平局")
            return
        else:
            continue
    if win(safe_list) == "1000" or win(safe_list) == "5050":
        return
    while 1:
        print("在进行下一步棋时%s将会消失" % (list_record[0]))
        who_get_chess(safe_player)
        location = input("下在哪里'输入数字1~9'")
        if str(location).isalpha():
            print("不可以输入字母")
            continue
        elif str(location) == "":
            print("请勿输入空")
            continue
        elif not str(location).isalnum():
            print("!!!输入数字1~9!!!")
            continue
        elif 1 > int(location) or 9 < int(location):
            print("超出范围!!!输入数字1~9!!!")
        elif safe_list[int(location) - 1] == "o" or safe_list[int(location) - 1] == "x":
            print("该位置已经有一个棋子了")
            continue

        safe_list[int(list_record[0]) - 1] = int(list_record[0])
        list_record.pop(0)

        if safe_player % 2 == 1:
            safe_list[int(location) - 1] = "x"
        else:
            safe_list[int(location) - 1] = "o"
        safe_player += 1
        checkerboard_print(safe_list)
        list_record.append(int(location))
        if win(safe_list) == "1000":
            print(str("%s子赢了" % (safe_list[int(location) - 1])))
            return
        elif win(safe_list) == "5050":
            return
        else:
            continue
    if win(safe_list) == "1000" or win(safe_list) == "5050":
        print("a")
        return


# 主函数
while 1:
    start_game = input("请输入您要游玩的类型：\n"
                       "1. 普通模式\n"
                       "2. 变化模式")
    start_game = int(start_game)

    if str(start_game).isalpha():
        print("不可以输入字母")
        continue
    elif str(start_game) == "":
        print("请勿输入空")
        continue
    elif not str(start_game).isalnum():
        print("!!!输入数字1 or 2!!!")
        continue
    elif int(start_game) == 1 or int(start_game) == 2:
        print("!!游戏开始!!<(￣︶￣)↗[GO!]")
        break

if start_game == 1:
    judge_checkerboard(list_number)
elif start_game == 2:
    after_6times_gaming(list_number)
