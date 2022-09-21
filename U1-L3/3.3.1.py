# 3.3.1 用户输入高度（行数），按照下方格式打印 1 个直角三角形
'''
*
**
***
****
*****
'''
hight = int(input("输入高度"))
for i in range (1 , hight + 1 , 1):
    print("*"*i)
