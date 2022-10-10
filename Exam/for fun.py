def sum_0(a):
    all_sum_list = []
    for _ in range(0,len(a)):
        for i in range(0,len(a)):
            if _ == i:
                continue
            else:
                for z in range(0,len(a)):#断智.jpg
                    if z == i or z == _:
                        continue
                    if a[_]+a[i]+a[z] == 0:
                        all_sum_list.append(tuple(sorted([a[_],a[i],a[z]])))
    return list(set(all_sum_list))
sample_list = [-1, 0, 1, 2, -1, -4, 0, 2, 0, 4, -4, -2, -1, 2]
print(sum_0(sample_list))