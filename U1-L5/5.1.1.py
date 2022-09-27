# 5.1.1 为以下列表尝试以上 14 种方法 / 函数 / 关键字，每一步操作后，打印当前的列表
list1 = []
num_list = [1, 2, 3, 4, 5]
num_list.insert(3, "a")
print('step 1 :', num_list)
num_list.append(2)
print('step 2 :', num_list)
list1.extend(num_list)
print('step 3 :', list1)
del num_list[2]
print('step 4 :', num_list)
del list1
num_list.remove(2)
print('step 6 :', num_list)
num_list.pop(3)
print('step 7 :', num_list)
num_list.clear()
print('step 8 :', num_list)
num_list.append(11)
num_list[0]=12
print('step 9 :', num_list)
num_list = [1,3,4,6,2,4,2,1]
num_list.sort()
print('step 10 :', num_list)
num_list.sort(reverse=True)
print('step 11 :', num_list)
num_list.reverse()
print('step 12 :', num_list)
print("tep 13 :",len(num_list))
print("tep 14 :",num_list.count(2))
