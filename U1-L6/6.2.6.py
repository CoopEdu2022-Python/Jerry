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
print(columnNumber("ZY"))

#好像写反了