# 6.1.6 定义一个函数，参数为 1 个字符串，将 a-z, A-Z 改为 z-a, Z-A，返回新的字符串
# 例如，参数为 'abcABC'，返回 'zyxZYX'
def turning(a):
    list_1 = []
    a = str(a)
    small_l = "abcdefghijklmnopqrstuvwxyz"
    big_l = small_l.upper()

    for _ in range(0,len(a)):
        for i in range(0,26):
            if a[_] == small_l[i] or a[_] == big_l[i]:
                if a[_].isupper() == True:
                    list_1.append(big_l[-i-1])
                else:
                    list_1.append(small_l[-i-1])
    result = "".join(list_1)
    return result
print(turning("abcABC"))
