def columnNumber(num):
    carry = 0
    result = 1
    num = list(num)
    list_al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(0,len(num)):

        result = (26**_)*carry + int(list_al.find(num[_])+1)
        carry = list_al.find(num[_])+1 + carry
        print(list_al.find(num[_])+1)
    return result
def altcolumnnimber(num):
    list_al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    carry = 0
    sum_ = 0
    safe_list = []
    while num > 0:
        safe_list.append(list_al[num - 1 % 26])
        num = (num-1)//26
    safe_list.append(list_al[carry])
    safe_list.append(list_al[num])

    return "".join(str(list_al))
print(altcolumnnimber(28))


#好像写反了
