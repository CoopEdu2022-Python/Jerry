def two_type(a,b):
    return str(bin(int(a,2)+int(b,2))).replace("0b","")
print(two_type("1010","11111"))