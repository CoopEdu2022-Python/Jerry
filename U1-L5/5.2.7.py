# 5.2.7 系统里面有多个用户，用户的信息目前保存在元祖中(一一对应），完成简单的登录功能
users = ('root', 'user1', 'user2')
passwords = ('123', 'abc', '@*#')
# 提示用户输入用户名和密码
# 如果登录成功，打印欢迎消息
# 如果失败，说明具体的错误原因，让用户重新登陆，共有 3 次机会
for i in range(0,3):
    username = input("请输入用户名")
    if username not in users:
        print("无该用户名")

    if username == users[j]:
        for x in range(0,len(passwords)):
            key = input("请输入密码")
            if key == passwords[x]:
                print("欢迎")
                break
            else:
                print("密码错误")
                continue
