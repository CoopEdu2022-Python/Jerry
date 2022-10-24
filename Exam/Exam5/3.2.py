def alter(n):
    n = int(n)
    if n >2**31:
        print("过头了")
    print(int(str("0b"+"0"* (32-int(len(str(bin(n)).removeprefix("0b"))))+str(bin(n)).removeprefix("0b")[::-1]).removeprefix("0b"),2))


alter(43261596)
n = 43261596
print(str("0b"+"0"* (32-int(len(str(bin(n)).removeprefix("0b"))))+str(bin(n)).removeprefix("0b")[::-1]).lstrip("0b"))