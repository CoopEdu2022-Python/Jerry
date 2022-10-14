def fanzhuan(n,t="123456789"):
    t = list(t)
    buzheng_1 = 0
    for i in range(0,len(t)//n+1):
        t.insert(i*n+buzheng_1," ")
        buzheng_1 += 1
    result = "".join(t)
    print(result)

    result = result.split()
    for _ in range(0,len(t)//n-1):
        result[_] = result[_][len(result[_])::-1]
    print(result)
    result = "".join(result)
    print(result)
fanzhuan(3)
#会有一个问题就是在n = 2 时会超出引索但是不知道12行怎么改
