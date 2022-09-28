#5.2.3 将 5.2.2 的函数复制过来，将返回值修改为一个元祖，这个元祖保存了所有学生的成绩
def mean():
    point_sum = 0
    n = int(input("学生数量"))
    list=[]
    for i in range(0,n):
        while 1 :
            grade = int(input("请输入成绩"))
            if 0<grade<100:
                list.append(grade)
                point_sum = point_sum +grade
                break
    all_print = (list,"平均成绩为：","%.2f" % (point_sum/n))
    return all_print
def true_print(a):
    for i in range(0, len(a)):
        print(a[i], end=" ")
true_print(mean())