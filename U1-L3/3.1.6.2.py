grade_sum = 0
for i in range(1,30):
    grade = int(input("输入分数"))
    while grade <= 0 or grade > 100:
        grade_sum = grade + grade_sum
        print(grade_sum)
print("录入完毕！平均分为%f.2分" % (grade_sum / 30))