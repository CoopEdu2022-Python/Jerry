# 5.3.3 下方是一个字典，按要求完成操作

dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
# ① 字典的长度是多少
print("字典长度为 %d"%len(dic))
print("*"*50)
# ② 请修改 'java' 这个 key 对应的 value 值为 98
dic['java'] = 98
print(dic['java'])
print("*"*50)
# ③ 删除 c 这个 key
dic.pop("c")
for all in dic.items():
    print(all)
print("*"*50)
# ④ 增加一个 key-value 对，key 值为 php, value 是 90
dic["php"] = 90
for all in dic.items():
    print(all)
print("*"*50)
# ⑤ 获取所有的 key 值，存储在列表里
key_list = []
for key in dic.keys():
    key_list.append(key)
print(key_list)
print("*"*50)
# ⑥ 获取所有的 value 值，存储在列表里
value_list = []
for value in dic.values():
    value_list.append(value)
print(value_list)
print("*"*50)
# ⑦ 判断 javascript 是否在字典中
print("javascript" in dic)
print("*"*50)
# ⑧ 获得字典里所有 value 的和
number_sum = 0
for value in dic.values():
    number_sum += value
print(number_sum)
print("*"*50)
# ⑨ 获取字典里最大的 value
value_list.sort()
print(value_list[0])
print("*"*50)
# ⑩ 获取字典里最小的 value
print(value_list[-1])
print("*"*50)
# ⑪ 字典 dic1 = {'php': 97}，将 dic1 的数据更新到 dic 中
dic1 = {'php': 97}
dic.update(dic1)
for all in dic.items():
    print(all)