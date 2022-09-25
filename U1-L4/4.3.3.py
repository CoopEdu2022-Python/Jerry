# 4.3.3 改写 #4.2.3：函数内不打印消息，将消息作为函数的返回值。调用 3 次函数，分别传入不同的参数，打印出不同的消息。并且，使用 2 种调用的方式
def make_shirt(size,juzi="I love Python"):

    return str("用户尺码为"+ size+", 在衣服上印刷句子："+juzi)
print(make_shirt(size="大"))
print(make_shirt(size="中"))
print(make_shirt(size="小" , juzi="随便"))
