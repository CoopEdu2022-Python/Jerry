list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import os
def checkerboard_print(list_number):
    os.system("cls")
    for _ in range(0, 3):

        for i in range(0, 3):
            print("| ", " ", end="|", sep="%s" % str(list_number[int(3 * _ + i)]))
        if _ == 2:
            break
        else:
            print("\n", "——--——--——--——-", sep="")
#好像是判断啊
def judge_checkerboard(list_number):
    for _ in range(0, 7):
        location = input("下在哪里")
        if str(location) == str(list_number[int(location)-1]):
            if _ % 2 == 1:
                list_number[int(location)-1] = "x"
            else:
                list_number[int(location)-1] = "o"
        else:
            print("不可以")
        checkerboard_print(list_number)
    return list_number

while 1:
    checkerboard_print(judge_checkerboard(list_number))
