#5.2.2 编写一个函数，功能是计算学生的平均分
# 用户先输入正整数 n，告知学生数量
# 用户输入每个学生的成绩，如果成绩在 0-100 以外，提示用户输入错误
# 学生成绩录入完毕后，计算平均分，将平均分作为返回值
# 在函数外部调用函数，打印出学生的平均分
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