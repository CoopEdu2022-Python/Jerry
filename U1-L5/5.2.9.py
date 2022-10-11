# 5.2.9 编写一个函数，功能是计算单人跳水比赛中的一次得分
# 单人项目跳水比赛时由 7 名裁判员分坐在跳台两侧的池岸上评分，最高 10 分，失败 0 分。
# 在计算分数时，去掉 2 个最高分和 2 个最低分，将 3 个中间分数相加之和，乘以动作的难度系数，就是动作的最终得分

def jump_water():
    a = []
    for i in range(0,7):
        while 1:
            x = int(input("打分"))
            if 0 <= x <= 10 :
                a.append(x)
                break
            else:
                print("打分有误")
    a.sort()
    new_list = a[2:-2]
    diffcuty_sorce = int(input("难度系数"))
    return (sum(list(new_list))*diffcuty_sorce)
print(jump_water())