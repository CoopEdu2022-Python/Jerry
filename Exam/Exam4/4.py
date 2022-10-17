def add_(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    a = len(num1.partition('.')[2])
    b = len(num2.partition('.')[2])
    n = max(a,b)
    bignum_a = num1.replace('.','')+('0'*(n-a))
    bignum_b = num2.replace('.','')+('0'*(n-b))
    sum = int(bignum_a) + int(bignum_b)
    sum = str(sum)
    if n > 0:
        if str(sum[:-n]+"."+sum[-n:]).startswith(".") == True:
            sum = "0" + sum[:-n] + "." + sum[-n:]
        else:
            sum = sum[:-n]+"."+sum[-n:]
    return sum

print(add_("0.9999999999", "0.0000000000009"))