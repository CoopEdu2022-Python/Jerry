def gcd_pro_max_2(*n):
    n = list(n)
    n.sort(reverse=True)
    while n[1] != n[len(n)-1]:
        for _ in range(0,len(n)-1):
            if n[_] % n [_+1] == 0:
                n[_] = n[_+1]
            else:
                n[_] = n[_] % n[_+1]
    return n[len(n)-1]

def gcd_pro_max_1(*n):
    if n[1] == n[len(n)-1]:
        return n[1]

print(gcd_pro_max_2(1, 2, 3, 4, 5))
print(gcd_pro_max_2(2, 4, 6, 8, 10))
print(gcd_pro_max_2(999, 1999, 2999, 3999, 4999))