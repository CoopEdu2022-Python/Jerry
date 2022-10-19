def digui(n):
    if n == 1:
        return n
    else:
        print(n)
        return n * digui(n-1)
print(digui(6))