# 定义函数 input_score
# - 允许用户输入 1 次成绩（0-100）、最多两位小数（可以是整数）
# - 如果输入的数字不符合要求，抛出自定义异常 ScoreError
# 在主程序中，完成 30 名学生成绩的录入，并捕获 2 类异常
# 1. 输入的不是数字
# 2. 输入的数字不符合要求
class ScoreError(Exception):
    pass


list_G = []


def input_score():
    a = float(input("输入成绩"))
    if a < 0 or a > 100:
        raise ScoreError("0-100")
    a = str(a) + ". "
    a = a.split(".")
    if len(a[1]) > 2:
        raise ScoreError("最多两位小数")
    list_G.append(a)


_ = 0
while _ < 3:
    try:
        input_score()
    except ScoreError:
        print(" 1. 输入的不是数字 2. 输入的数字不符合要求")
    else:
        _ += 1
