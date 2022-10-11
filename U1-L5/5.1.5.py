# 5.1.5 定义一个函数，作用是将列表中的数字元素全部扩大两倍，其他类型保持不变，修改完成后，将新列表作为返回值
def alter(a):
    for i in range(0,len(a)):
        if type(a[i]) == int or type(a[i]) == float:
            a[i] = (a[i]) * 2
        else:
            continue
    return a

print(alter([1,7,9,8,6,6.6,"u"]))