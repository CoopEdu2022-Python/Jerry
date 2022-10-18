def pali(a):
    a = list(a)
    list = []
    for _ in range(0,len(a)):
        if str(a[_]).isalnum() or str(a[_]).isalpha():
            b = str(a[_]).lower()
            list.append(b)

    return  list
print(pali(["addaadad"]))