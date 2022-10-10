def sda(a):
    connect_list = []
    for _ in range(0,len(a)):
        for i in range(_+1,len(a)):
            if _ == i:
                continue
            else:
                for z in range(i+1,len(a)):#断智.jpg
                    if z == i or z == _:
                        continue
                    else:
                        connect_list.append(a[_]*a[i]*a[z])

    print(list(sorted(connect_list))[-1])
sda([1, 2, -3, -3, 7,6,5,0])