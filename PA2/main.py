
databeenread = ''


def login_main(account, password):
    pass


def add_student(account, name):
    file = open("id_data.txt", mode="a")
    file.writelines([str(account), "|", "123456", "|", str(name), "|", "student", "|","no class", "|", "2学分", "\n"])
    file.close()

    return


def readlen():
    count = len(open("id_data.txt", 'r').readlines())
    print(count)
    return count


def check_account(account, password):
    first = open("id_data.txt", mode="r")  # 返回一个文件对象
    line = first.readline()  # 调用文件的 readline()方法
    while line:
        if line[:len(account) + 1] == account + "|":
            while line[len(account) + 1:len(account) + 2 + len(password)] != password + "|":
                print("您输入的:" + password + " 是错误密码")
                password = str(input("请重试密码"))
            global databeenread
            databeenread = line
            return True
        line = first.readline()
    first.close()
    print("未查询到该账号")
    return False


def userboard():
    datare = databeenread.split("|")
    print(datare)
    click = input("可输入'用户身份','课程信息','学分要求;")
    boardlist = {"用户身份": datare[3], "课程信息": datare[4], "学分要求": datare[5]}
    print(boardlist[click])


add_student(121212, "刘行")
add_student(1238923, "sdans")
add_student(123, "sddns")
lenoflist = readlen()
print(lenoflist)

while 1:
    if check_account(str(input("请输入账号'测试账号为:123'")), str(input("请输入密码'测试账号为:123456'"))):
        break
print("欢迎进入选课系统")
print(databeenread)
while 1:
    userboard()
