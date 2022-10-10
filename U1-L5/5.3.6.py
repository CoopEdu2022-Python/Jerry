# 5.3.6 编写一个函数 compare_dict(dict1, dict2)，判断两个字典中存在多少个完全相同的键值对，将重复键值对的数量和重复的键值对保存在一个元祖中，将这个元祖作为返回值
list_a = {1:3,2:5,8:9}
list_b ={1:3,4:6,8:9}
list_d = []
def compare_dict(dict1, dict2):
    for _ in dict2.keys():
        if dict1.get(_) is None:
            continue
        if dict2[_] == dict1[_]:
            list_d.append({_:dict2[_]})
        continue

compare_dict(list_a,list_b)
all_tuple = (list_d)
print(all_tuple)