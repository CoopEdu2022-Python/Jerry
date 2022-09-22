m = int(input("请输入一个数字"))
n = int(input("请输入另外一个数字"))
x = int(0)
c = int(0)
d = int(0)
for i in range(1,n+1):

    for a in range(0,i):
        c = m*(10**a)
        x = x + c


print(x)

