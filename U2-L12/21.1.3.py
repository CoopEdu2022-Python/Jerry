file = open("1 .txt", "r+")
x=[]
while 1:
    a = file.readline().replace("\n","")
    if a[0] != "#":
        print(a)
        x.append(a[1::])


file.close()
#这个引索怎么操作