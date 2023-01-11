def big_add(num1, num2):

    n1 = len(num1.partition('.')[2])
    n2 = len(num2.partition('.')[2])
    n = max(n1, n2)


    num1 = num1.replace('.', '') + ('0' * (n - n1))
    num2 = num2.replace('.', '') + ('0' * (n - n2))
    sum_final = str(int(num1) + int(num2))


    # 使用 Python 的大数加法


    # 有小数时添加小数点
    if n > 0:
        sum_final = sum_final[:-n] + '.' + sum_final[-n:]
    if sum_final[0] == "-" and sum_final[1] == ".":
        sum_final = "-0"+sum_final[1:]
    if sum_final[0] == ".":
        sum_final = "0"+sum_final
    return sum_final

print(big_add('1', '2'))  # 3
print(big_add('1', '0.2'))  # 1.2
print(big_add('1', '-0.2'))  # .8
print(big_add('0.1', '0.2'))  # .3
print(big_add('0.1', '0.9'))  # 1.0
print(big_add('0.1', '-0.1'))  # .0
print(big_add('-0.1', '-0.2'))  # -.3