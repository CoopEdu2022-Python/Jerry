import random
for a in range(0,40):
    x = 0
    for _ in range(0,7):
        i = random.randint(1,6)
        if i == 2:
            x += 1
    print(x, end=" ")