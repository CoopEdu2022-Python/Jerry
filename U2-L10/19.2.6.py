def count_operations(num1: int, num2: int) -> int:
    a = 0
    while 1:
        if num1 == 0 or num2 == 0:
            return a
        if num1 >= num2:
            num1 = num1-num2

        else:
            num2 = num2 - num1
        a += 1
print(count_operations(num1 = 2, num2 = 3))