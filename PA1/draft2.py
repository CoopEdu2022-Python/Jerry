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
        return "结束了"


# 输入输出棋子数量——操作
def judge_checkerboard(safe_list):
    save_listBefore = []
    for _ in range(0, 7):
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
        if win(safe_list):
            print(str("%s子赢了" % (safe_list[int(location) - 1])))
            return "游戏结束了"
        else:
            continue
    if win(safe_list):
        return

# 判断输赢
def win(safe_list):
    safe_list = list(safe_list)
    if safe_list[0] == safe_list[1] == safe_list[2] or safe_list[2] == safe_list[5] == safe_list[8] or \
            safe_list[6] == safe_list[7] == safe_list[8] or safe_list[0] == safe_list[3] == safe_list[6] or \
            safe_list[6] == safe_list[4] == safe_list[2] or safe_list[8] == safe_list[4] == safe_list[0] or \
            safe_list[3] == safe_list[4] == safe_list[5] or safe_list[7] == safe_list[4] == safe_list[1]:
        return True
    else:
        return False


def after_7times_gaming(safe_list, save_listBefore):
    print(safe_list)


while 1:
    checkerboard_print(judge_checkerboard(list_number))
