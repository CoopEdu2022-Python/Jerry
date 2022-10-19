def hahanumber(a):
    sum_a = int(a)
    a = str(a)
    list_ = []
    while sum_a != 1:
        for _ in range(0,len(a)):
            list_.append(int(a[_])**2)
        sum_a = sum(list_)
        if hahanumber(sum_a) == True:
            break

    return True

print(hahanumber("19"))