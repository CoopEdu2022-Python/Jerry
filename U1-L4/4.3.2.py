# 4.3.2 改写 #4.2.2：函数内不打印消息，将消息作为函数的返回值。调用函数时，在 print 语句中直接调用函数，打印提示信息
def chengshan():
    juzi = str(input("需要印刷啥"))
    size = int(input("你要几号的衣服"))
    alter =str(size)
    return str("用户尺码为:"+ alter +" ,在衣服上印刷句子:"+juzi)
print(chengshan())