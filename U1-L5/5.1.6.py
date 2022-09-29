def change(a):
    for i in range(0,(len(a)*2)-1):
        if i % 2 != 0:
            a.insert(i,0)
        else:
            continue
    return a
print(change([1,7,9,8,6,"u",9,7,5]))