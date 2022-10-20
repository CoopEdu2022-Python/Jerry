def f(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    else:
        return f(a-1)+f(a-2)
def fi(a):
    if a == 1:
        return 1
    else:
        return f(a-1)+1+f(a-1)
print(fi(9))

print(f(19))
