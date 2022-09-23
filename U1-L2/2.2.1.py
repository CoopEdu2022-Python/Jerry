# 2.2.1 用两种不同的逻辑嵌套方式，完成火车站安检的例子
safe = str(input("你有杯子吗？"))
if safe == "是" and "有":
    safe = float(input("水杯中的液体有多少毫升"))
    if safe > 200.0 :
        print("你不能走，这鸡汤甚是美味啊")
    else:
        print("走吧")
else:
    print("下一个")
next_2 = str(input("你有杯子吗？"))
next_1 = float(input("水杯中的液体有多少毫升"))

if (next_1>200 or next_2 =="有" or next_2 == "是"):
    next_3 = str(input("会不会爆炸"))
    if next_3 == "不会":
        print("再检查检查")
    else:
        print("诶！ 自首了！抓起来抓起来")
else:
    print("下一个")