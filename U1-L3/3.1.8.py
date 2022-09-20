# 3.1.8 分别计算 1 到 100 中所有奇数、偶数的和
all_number_start = -1
ji = 0

while all_number_start < 100:

    all_number_start = all_number_start + 1
    while all_number_start % 2 == 0:
        ji = all_number_start + ji
        break
print("奇SUM",ji)

all_number_start = -1
ou = 0

while all_number_start < 100:

    all_number_start = all_number_start + 1
    while all_number_start % 2 != 0:
        ou = all_number_start + ou
        break
print("偶SUM",ou)
