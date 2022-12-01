file = open("3.txt","r")
file1 = open("jiami.txt","w+")
a = file.read()
find="abcdefghijklmnopqrstuvwxyz"
find2="ABCDEFGHIJKLMNOPQRSTUVWXYZA"
for _ in range(len(a)):
    if a[_] in find:
        for i in range(len(find)):
            if a[_] == find[i]:
                file1.write(find[i-1])
    elif a[_] in find2:
        for i in range(len(find2)):
            if a[_] == find2[i]:
                file1.write(find2[i + 1])
    else:
        file1.write(a[_])
print(a)
file.close()