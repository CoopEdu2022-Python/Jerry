def gcd_pro_max_2(*n):
    n = list(n)
    while len(set(n))>1:
        n.sort(reverse=True)
        for _ in range(0,len(n)-1):
            if n[_] % n [_+1] == 0:
                n[_] = n[_+1]
            else:
                n[_] = n[_] % n[_+1]
    return set(n).pop()

def gcd_pro_max_1(*n):
    n = list(n)

    if len(set(n)) == 1:
        return set(n).pop()
    n.sort(reverse=True)
    for i in range (len(n)-1):
        if n[i] % n[i+1] == 0:
            n[i] = n[i+1]
        else:
            n[i] = n[i] % n[i+1]
    return gcd_pro_max_1(*n)

print(gcd_pro_max_1(1, 2, 3, 4, 5))
print(gcd_pro_max_1(2, 4, 6, 8, 10))
print(gcd_pro_max_1(999, 1999, 2999, 3999, 4999))
print(gcd_pro_max_2(999, 1999, 2999, 3999, 4999))