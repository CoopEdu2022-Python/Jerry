def how_count(n):
    n=str(n)
    cunt = 0
    if len(n) > 8:
        cunt += 1
    for i in range(0,len(n)):
        if n.isalnum() == True:
            cunt += 1
            break
    for i in range(0, len(n)):
        if n.isalpha() == True:
            cunt += 1
            break
    for i in range(0, len(n)):
        if n.isupper() == True:
            cunt += 1
            break
    if cunt >= 2:
        return True
    else:
        return False
def reset_key():

    login_info = {'root':'123', 'user1':"abc", 'user2':"@*#"}
    while 1:
        username = input("请输入用户名")
        if username not in login_info.keys():
            print("无该用户名")
            continue
        for _ in range(3):
            if username in login_info.keys():
                key = input("请输入密码")
                if login_info[username] != key:
                    print("原密码错误")
                else:
                    print("密码正确")
                    break


        while 1:
            new_psssword = input(str("输入你要更改的密码"))
            if how_count(new_psssword) == True:
                login_info[username] = new_psssword
                secound_compair = input(str("再次输入你要更改的密码"))
                if secound_compair !=new_psssword:
                    print("两次密码不一样")

                else:
                    return login_info
            else:
                print("错误")

                continue
        break



print(reset_key())