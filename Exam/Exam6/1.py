# 定义一个函数 is_power_of_3_v1(n)，参数为整数，判断 n 是否为 3 的幂
# 定义另一个函数 is_power_of_3_v2(n)，用另一种方式，判断 n 是否为 3 的幂
# n 的取值范围为 -2^31 <= n <= 2^31 - 1
def is_power_of_3_v1(n: int) -> bool:
    while 1:
        if n % 3 == 0:
            while 1:
                n = n / 3
                if n == 1:
                    return True
                else:
                    break
        elif n % 3 < 3:
            return False
        else:
            n = n / 3
def is_power_of_3_v2(n) -> bool:
    if n == 1:
        return True
    if n % 3 == 0:
        return is_power_of_3_v2(n/3)
    else:
        return False
def is_power_of_3_v3(n):
    safe_list = []

    for _ in range(0,32):
        x = 3 ** _
        safe_list.append(x)
    return n in safe_list

print(is_power_of_3_v1(27))
print(is_power_of_3_v2(9))
print(is_power_of_3_v3(6))