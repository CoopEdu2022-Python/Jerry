def add_one(list1):
    list1 = list(list1)
    num1 = "".join([str(num) for num in list1])
    num1 = int(num1) + 1
    list1 = list(str(num1))
    return list1

print(add_one([1,2,3,4,5]))

