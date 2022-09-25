# 4.3.4 改写 #4.2.4：函数内不打印消息，如果输入的城市和国家匹配，将返回值设置为 'YES'；如果不匹配，将返回值设置为 'NO'。
# 调用 3 次函数，传入不同的参数，输出不同的结果。并且，使用 2 种调用的方式
def describe_city(c,t_f,n="Beijing"):
    return str(c+" is in "+n+" is "+t_f)
print(describe_city(c = "Xiangang",t_f="YES"))
print(describe_city(c = "Zhejiang",t_f="YES"))
print(describe_city(c="Newyork",t_f="NO"))