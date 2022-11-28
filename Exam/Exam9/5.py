def fill_cups(amount: list[int]) -> int:
    a = 0
    while 1:
        amount.sort()
        if amount[2] ==0:
            return a

        if amount[0] != 0:
            amount[0] -= 1
            amount[2] -= 1
            a += 1
            continue
        elif amount[1] != 0:
            amount[1] -= 1
            amount[2] -= 1
            a += 1
            continue
        else:
            a = a + amount[2]
            return a
print(fill_cups([1,4,2]))