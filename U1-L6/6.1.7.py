# 6.1.7 定义一个函数，参数为 1 个字符串和 1 个只包含字符串的列表，用字符串作为连接符，将列表的每个元素连接起来，返回连接后的字符串
# 例如，参数为 '123' 和 ['a', 'b', 'c']，返回 'a123b123c'
def cha(a,b):
    a = str(a)
    b = list(b)
    b = "".join(b)
    return b.join(a)
print(cha('123',['a', 'b', 'c']))