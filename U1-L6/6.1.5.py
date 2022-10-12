# 6.1.5 定义一个函数，参数为 1 个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数，将所有数量保存在 1 个元祖返回
def count(a):
    a = str(a)
    kong = 0
    other = 0
    sum_alph = 0
    sum_num = 0
    kong += a.count(" ")
    for _ in range(0,52):
        sum_alph += a.count("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"[_])
    for i in range(0,10):
        sum_num += a.count("1234567890"[i])
    other = len(a) - sum_alph - kong - sum_num
    return list(tuple(sum_alph,kong,sum_num,other))

print(count(input("shuru")))