# 3.3.5 有 1 2 3 4 四个数字，组成互不相同且无重复数字的 3 位数，打印出所有结果
k=0
for i in range(1,5,1):
    for a in range(1,5,1):
        for b in range(1,5,1):
            if i == a or a==b or i==b:
                continue
            else:
                k +=1
                print(i, a,b)
print(k)