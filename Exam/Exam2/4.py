
for g in range(1,10):

    for s in range(1,10):

        for b in range(1,10):
            if (g**3 + s**3 + b**3)==g*100+s*10+b:
                print(g,s,b,end="   ",sep="")
                b= b+1
        s = s+1

    g=g+1

