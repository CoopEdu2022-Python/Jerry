# 3.3.2 用户输入高度（行数），按照下方格式打印 1 个菱形
'''
  *
 ***
*****
 ***
  *
'''
hight = int(input("输入高度"))
if hight % 2 == 0:
    print("别输入偶数啊Σ(っ °Д °;)っ")
else:
    a = 1
    for i in range (1 , hight+1  , 2):
        a = a + 1
        print(" "* (hight - a) ,end="",sep="")
        print("*"*i)
    for i in range (hight-2 , 0 , -2):
        a = a -1
        print(" "* (hight - a) ,end="",sep="")
        print("*"*i)


