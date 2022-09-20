# 3.1.8 分别计算 1 到 100 中所有奇数、偶数的和

odd = 0
even = 0
for i in range(1,101,1):
    if i % 2 == 0:
        even = i + even
    else:
        odd = i + odd
print(even,odd)