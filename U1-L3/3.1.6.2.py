sum = 0
grade_sum = 0
for i in range(0,3):
    while 1:
        num = int(input())
        if num > 100 or num < 0 :
            print("错")
        else:
            sum += num
            break
print("录入完毕！平均分为%f分" % (sum /3))