import os
databeenread = ''
student_way = None

def login_main(account, password):
    pass


def add_student(account, name):
    account = str(account)
    print(os.listdir('students'))
    global student_way
    student_way = "C://Users/徐洪森/PycharmProjects/pythonProject/all project/PA2/students/"
    imformation = [str(account), "|", "123456", "|", str(name), "|", "student", "|","no class", "|", "2学分"]
    full_name = student_way + account + ".txt"
    file = open(full_name, mode="w")
    file.write(str(imformation))
    file.close()

    return


def readlen():
    count = len(open("id_data.txt", 'r').readlines())
    return count


def check_account(account, password):
    for _ in range(len(os.listdir('students'))):
        if str(account)+".txt"  == os.listdir("students")[_]:
            filer = open(student_way + os.listdir("students")[_],mode="r")
            linesread = filer.readlines()
            print(linesread)
        else:
            print("None")
            print(os.listdir("students")[_])
    # first = open("id_data.txt", mode="r")  # 返回一个文件对象
    # line = first.readline()  # 调用文件的 readline()方法
    # while line:
    #     if line[:len(account) + 1] == account + "|":
    #         while line[len(account) + 1:len(account) + 2 + len(password)] != password + "|":
    #             print("您输入的:" + password + " 是错误密码")
    #             password = str(input("请重试密码"))
    #         global databeenread
    #         databeenread = line
    #         return True
    #     line = first.readline()
    # first.close()
    # print("未查询到该账号")
    # return False


def userboard(click):
    datare = databeenread.split("|")
    print(datare)
    boardlist = {"用户身份": datare[3], "课程信息": datare[4], "学分要求": datare[5]}
    print(boardlist[click])


add_student(121212, "刘行")
add_student(1238923, "sdans")
add_student(123, "sddns")
lenoflist = readlen()
check_account("123","21323")
# while 1:
#     while 1:
#         if check_account(str(input("请输入账号'测试账号为:123'")), str(input("请输入密码'测试账号为:123456'"))):
#             break
#     print("欢迎进入选课系统")
#     print(databeenread)
#     while 1:
#         click = input("可输入'用户身份','课程信息','学分要求','登出'")
#         if click == "登出":
#             break
#         userboard(click)
