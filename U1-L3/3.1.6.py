# 3.1.6 一次考试后，循环录入某班级 30 名学生的成绩，并计算平均分
# 如果分数超过 100 或小于 0，提示“分数有误，请重新输入”
# 30 名学生的成绩输入完成后，提示“录入完毕！平均分为 xx 分”，并结束程序
x = 0
grade_sum = 0

while x != 31 :
    grade = 0
    while grade <= 0 or grade > 100:
        grade = int(input("输入分数"))
    grade_sum = grade + grade_sum
    x = x + 1
    print(grade_sum)
print("录入完毕！平均分为%f.2分" % (grade_sum / 30))