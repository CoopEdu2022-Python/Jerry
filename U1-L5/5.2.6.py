# 5.2.6 小明在黑板上写了一个整数数列，先将数列由小到大排好，每次擦去其中的第 1 个和第 2 个数，
# 假设擦去数的值分别为 a 和 b，再在数列中添加一个数 a * b + 1 并保持数列有序，如此下去，直至黑板上只剩下一个数，打印出这个数
def cut_number(list):

    while 1:
        if len(list) <= 1:
            return list
        int_1 = 0
        list.sort()
        int_1 = list[0] * list[1]+1
        list.append(int_1)
        list.sort()
        list.pop(0)
        list.pop(0)

a = [1,7,9,6,3]
print(cut_number(a))
