# 1. 什么是异常？
"""执行时检测到的错误称为异常
"""
# 2. 异常有哪些类型？（如何找到全部的异常类型？)
print([name for name in dir(BaseException) if name[:2]!="__"and name [::-1][:2] != "__"]) # 不知道存在Exception自带的异常在哪里

# 3. 如何捕获异常？
"""try:
    尝试执行的代码
except 异常类型1:
    针对异常类型1，对应的处理代码
except 异常类型2:
    针对异常类型2，对应的处理代码
except:
    出现异常，执行的代码
except Exception as result:捕获未知异常
    pass
else:
    没有异常，执行的代码
finally:
    无论是否有异常，都会执行的代码"""

# 4. 如何抛出异常？
#条件…………
"""a = Exception("AAAA")
raise a"""

# 5. 什么是异常的传递？
"""当函数/方法执行出现异常就会将异常传递给函数/方法的调用一方直到传递到主函数爆出异常"""