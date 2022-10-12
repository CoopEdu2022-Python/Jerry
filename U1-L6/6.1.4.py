# 6.1.4 定义一个函数，参数为 2 个字符串，从第 1 个字符串中删除第 2 个字符串中所有的字符，返回新的字符串
# 例如，参数为 'They are students.' 和 'aeiou'，返回 'Thy r stdnts.'
def cut(a,b):
    a = list(str(a))
    b = list(str(b))
    for _ in range(0,len(a)):
        for i in range(0,len(b)):
            if a[_] != b[i]:
                continue
            else:
                a[_] = ""
    return (''.join(a))
print(cut('They are students.','aeiou'))
#居然可以！！！