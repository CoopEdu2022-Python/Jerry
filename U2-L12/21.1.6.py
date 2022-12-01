file = open("4.txt","r")
file1 = open("jiami2.txt","w+")
a = file.read()
find="abcdefghijklmnopqrstuvwxyz"
find2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(len(a)):
    if a[_] in find:
        file1.write(a[_].upper())
    elif a[_] in find2:
        file1.write(a[_].lower())
    else:
        file1.write(a[_])