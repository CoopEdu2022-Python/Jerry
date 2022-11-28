# 在 try……finally 结构中，无论 try 语句是否出现异常，finally 语句都会执行
# 在函数中，finally 的执行顺序在 return 之前还是之后？
# 设计一段代码，探究以上问题，在设计并运行代码后，用多行注释简单说明 finally 的执行机制
def test():
    try:
        a = int(input("number"))
        return a
    except ValueError("damie"):
        pass
    finally:
        print("finally")
print(test())#看finally和a的值哪个先输出
# number2
# finally
# 2
# finally先输出意味着finally优先级更高。
