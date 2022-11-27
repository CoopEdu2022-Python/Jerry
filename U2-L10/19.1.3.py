# 19.1.3  分母异常
# 定义一个函数，参数为两个数字 a，b，计算 a / b 的值
# 如果 b 等于零，抛出异常
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        e = Exception("除数为零")
        raise e
print(division(2,0))
#为啥会报两次错呢？
