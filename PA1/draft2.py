import os

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 将列表打印为图像
def checkerboard_print(safe_list):
    safe_list = list(safe_list)
    if win(safe_list) == False:
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
        print("\n","游戏结束了")
        return


# 输入输出棋子数量——操作
# 同时也是第一阶段
def judge_checkerboard(safe_list):
    save_listBefore = []
    _ = 0
    while 1:

        while 1:
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
            elif safe_list[int(location) - 1] == "o" or safe_list[int(location) - 1] == "x":
                print("该位置已经有一个棋子了")
                continue


            else:
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


# 判断输赢
def win(safe_list):
    safe_list = list(safe_list)
    if 1 in safe_list or 2 in safe_list or 3 in safe_list or 4 in safe_list:
        if safe_list[0] == safe_list[1] == safe_list[2] or safe_list[2] == safe_list[5] == safe_list[8] or \
                safe_list[6] == safe_list[7] == safe_list[8] or safe_list[0] == safe_list[3] == safe_list[6] or \
                safe_list[6] == safe_list[4] == safe_list[2] or safe_list[8] == safe_list[4] == safe_list[0] or \
                safe_list[3] == safe_list[4] == safe_list[5] or safe_list[7] == safe_list[4] == safe_list[1]:
            return "1000"
        else:
            return False
    else:
        return "5050"
# 二阶段加上原有，变化玩法。
def after_7times_gaming(safe_list):
    for _ in range(0,9):
        while 1:
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
            elif safe_list[int(location) - 1] == "o" or safe_list[int(location) - 1] == "x":
                print("该位置已经有一个棋子了")
                continue


            else:
                break
        if str(location) == str(safe_list[int(location) - 1]):
            if _ % 2 == 1:
                safe_list[int(location) - 1] = "x"
            else:
                safe_list[int(location) - 1] = "o"
        checkerboard_print(safe_list)
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


judge_checkerboard(list_number)
