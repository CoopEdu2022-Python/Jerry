# 5.3.5 编写一个函数 update_dict(dict_sample)，功能如下
# 用户输入一个 key-value（分 2 次输入），value 为数字类型，key 为 str 类型
# 如果原有的 dict_sample 中没有用户输入的 key，就添加这个 key-value
# 如果原有的 dict_sample 中存在用户输入的 key，保留较大的 value
# 将修改后的字典作为返回值

def update_dict(dict_sample):
    import_key = str(input("key"))
    import_value = int(input("value"))
    for _ in dict_sample.keys():
        if _ == import_key:
            if dict_sample[_] <= import_value :
                dict_sample[_] = import_value
        else:
            a = ({import_key:import_value,})
    dict_sample.update(a)
    return dict_sample
dict_sample = {"sdawd":3,"e":5,"dfsfdf":7}
print(update_dict(dict_sample))
