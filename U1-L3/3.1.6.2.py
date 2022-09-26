sum_g = 0
grade_sum = 0
for i in range(1,31):
    while 1:
        num = int(input())
        if num > 100 or num < 0 :
            print("错")
        else:
            sum_g += num
print("录入完毕！平均分为%f.2分" % (grade_sum / 30))