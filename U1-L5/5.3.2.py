# 5.3.2 按要求操作下方的字典
# ① 循环遍历所有的 key
# ② 循环遍历所有的 value
# ③ 循环遍历出所有的 key 和 value
dict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for key in dict.keys():
    print(key , end=" ")
print("\n")
for value in dict.values():
    print(value , end=" ")
print("\n")
for all in dict.items():
    print(all , end=" ")
print("\n")