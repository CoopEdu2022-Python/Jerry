import random
a = []
for i in range(0,1):
    x = random.randint(0,6)
    if x in a:
        continue
    a.append(x)
print(a)

