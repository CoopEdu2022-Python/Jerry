while 1:
    a = float(input("请输入一个数字"))
    b = float(input("请输入另外一个数字"))
    way = str(input("选择计算方法输入“加“，“减”，”乘”，“除”"))
    if b == 0:
        print("零不可以作为除数")
    else:
        if way == "加":
            print(a+b )
        elif way == "减":
            print(a-b )
        elif way == "乘":
            print(a*b )
        elif way == "除":
            print(a/b)
