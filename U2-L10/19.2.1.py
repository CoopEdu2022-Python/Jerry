# 让用户输入 2 个整数 start 和 end，打印这两个整数之间（包含两端）的一个随机整数
# 考虑用户输入不是整数的情况，以及 start > end 的情况，抛出异常并处理
import random

def startend(a,b):

    if str(a).isdigit() == False or str(b).isdigit() == False:
        raise Exception("不是整数")
    if a > b:
        raise Exception("start > end")

    return random.randint(a, b)


print(startend(9,4))

