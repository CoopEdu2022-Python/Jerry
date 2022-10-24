def reset_key():

    login_info = {'root':'123', 'user1':"abc", 'user2':"@*#"}
    while 1:
        username = input("请输入用户名")
        if username == "q":
            return
        if username not in login_info.keys():
            print("无该用户名")
            continue
        if username in login_info.keys():
            key = input("请输入密码")
            if len(login_info) > 3:
                print("超出上限")
                break
            if login_info[username] != key:

                print("密码错误")
                continue
            while 1:
                new_psssword = input(str("输入你要更改的密码"))
                if new_psssword.isalnum() == False or new_psssword.isalpha() == False and len(new_psssword)>8:
                    login_info[username] = new_psssword
                    return login_info
                else:
                    print("错误")

                    continue
        break


print(reset_key())