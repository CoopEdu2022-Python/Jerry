import random
a = []
for i in range(0,80):
    x = random.randint(1, 800)
    if x in a:
        continue
    a.append(x)
print(a)

