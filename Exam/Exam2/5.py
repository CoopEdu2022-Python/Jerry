
c=0
for a in range(3,1000):
    for i in (2 , a):
        if a % i ==0:
            if i == a:
                break
            elif i != a:
                while a % i == 0:
                    c = i + c
                    if c == a:
                        print(c)
                    a = a / i
                    continue


        else: i =i+1

