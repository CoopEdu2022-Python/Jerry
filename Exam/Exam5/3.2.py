def alter(n):
    n = int(n)
    if n >2**31:
        print("过头了")
    print(int(("0b"+(0* (32-(len(str(bin(n)).lstrip("0b"))))+str(bin(n)).lstrip("0b")[::-1])),2))


alter(43261596)
