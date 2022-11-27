# 定义一个函数，函数的参数为一个字符串，获取用户的输入
# 主程序中，用户一次性输入 5 个数，以逗号分隔
# 函数需要将用户输入的数字提取出来，存入列表并返回这个列表
# 如果输入数据不为整数，要捕获产生的异常，打印 '请输入整数'
# 捕获输入参数不足 5 个或超过 5 个的异常，打印 '请输入 5 个整数
def list_get():
    list1 = str(input("请输入五个数"))
    list1 = list1.split(",")
    if len(list1) != 5:
        print(len(list1))
        out = Exception("请输入 5 个整数")
        raise out
    for _ in range(len(list1)):
        if str(list1[_]).isdigit() is not True:
            no = Exception("请输入整数")
            raise no
    return list1
print(list_get())