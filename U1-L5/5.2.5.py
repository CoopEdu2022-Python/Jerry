
# 5.2.5 处理矩阵
# 使用 for 循环，将下方的矩阵保存在一个二维列表中
# 定义 2 个元祖，一个保存行，一个保存列，元祖的每个元素是一个列表（一行或一列的所有数），打印这 2 个元祖
# 定义 2 个新的元祖，分别保存行、列的和，打印这 2 个元祖
'''
  1  2  3  4  5  6
  7  8  9 10 11 12
 13 14 15 16 17 18
 19 20 21 22 23 24
 25 26 27 28 29 30
 31 32 33 34 35 36
'''
def total_print(a):
    for i in range(0,len(a)):
        print(a[i],sum(a[i]))


list = []
a = 1
for i in range (0,6):
    other_list = []
    for b in range (0,6):
        other_list.append(a)
        a += 1
    list.append(other_list)
print(list)
x=(list,)
total_print(list)

sum_list = []
for e in range (0,6):
    newlist = []
    for b in range (0,6):
        newlist.append(list[b][e])
    sum_list.append(newlist)
print(sum_list)
oto = (sum_list,)
total_print(sum_list)