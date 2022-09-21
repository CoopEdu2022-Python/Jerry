import time
for a in range(1,101):
    print("\b"*5,end="")
    print(a,"%",end="",sep="")
    time.sleep(0.1*a)
    a += 1

