import os
from student import Student
from teacher import Teacher
save_data = ''
databeenread = ''
student_way = "students/"

def login_main(account, password):
    pass


def add_student(account, name):
    account = str(account)
    print(os.listdir('students'))
    global student_way
    student_way = "students/"
    imformation = str(account), "123456", str(name), "student",["no class"],""
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
            while 1:
                if linesread[0].split(",")[1].split("'")[1] == password:
                    global save_data
                    save_data = linesread[0]
                    return linesread[0].split(",")[3].split("'")[1]

                else:
                    print("密码错误")
                    password = input("请重新输入密码")


    return ("未查询到该账号")
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

    boardlist = {"用户身份": user.get_self(), "课程信息": user.course}
    return boardlist[click]

def lon_in():
    while 1:
        s_c = str(input("请输入账号'学生测试账号为:123，教师测试账号为:1234"))
        s_p = str(input("请输入密码'学生与教师测试账号密码为都:123456'"))
        if check_account(s_c, s_p) == "student":

            student_user = Student(save_data.split(",")[0], save_data.split(",")[1], save_data.split(",")[2],
                        save_data.split(",")[3], save_data.split(",")[4])
            return student_user
        elif check_account(s_c, s_p) == "teacher":

            teacher_user = Teacher(save_data.split(",")[0], save_data.split(",")[1], save_data.split(",")[2])
            return teacher_user
        print(check_account(s_c, s_p))



while 1:
    user = lon_in()
    print("欢迎进入选课系统")
    while 1:
        if user.user_board() == "break":
            break


