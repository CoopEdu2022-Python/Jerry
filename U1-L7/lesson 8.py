def f(a):
    if a == 1:
        return 1
    else:
        return f(a-1)+1+f(a-1)
print(f(9))