list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import os
def checkerboard_print(list_number):
    if win(list_number) == False:
        os.system("cls")
        for _ in range(0, 3):

            for i in range(0, 3):
                print("| ", " ", end="|", sep="%s" % str(list_number[int(3 * _ + i)]))
            if _ == 2:
                break
            else:
                print("\n", "——--——--——--——-", sep="")
    else:
        return "已经结束了"
#好像是判断啊
def judge_checkerboard(list_number):
    for _ in range(0, 7):
        while 1:
            location = input("下在哪里")
            if str(location).isalpha() == True:
                print("不可以输入字母")
                continue
            elif str(location) == "":
                print("请勿输入空")
            else:
                break
        if str(location) == str(list_number[int(location) - 1]):
            if _ % 2 == 1:
                list_number[int(location) - 1] = "x"
            else:
                list_number[int(location) - 1] = "o"
        checkerboard_print(list_number)
        if win(list_number) == True:
            print(str("%s子赢了" % (list_number[int(location) - 1])))
            return list_number

        else:continue
    return list_number

def win(list_number):
    if list_number[0] == list_number[1] == list_number[2] or list_number[2] == list_number[5] == list_number[8] or list_number[6] == list_number[7] == list_number[8] or list_number[0] == list_number[3] == list_number[6] or list_number[6] == list_number[4] == list_number[2] or list_number[8] == list_number[4] ==list_number[0] or list_number[3] == list_number[4] == list_number[5] or list_number[7] == list_number[4] == list_number[1]:
        return True
    else:
        return False
def after_7times_chessing():

while 1:
    checkerboard_print(judge_checkerboard(list_number))
