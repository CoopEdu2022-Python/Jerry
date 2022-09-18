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

if (next_1>200 or next_2 =="有" and "是"):
    next_3 = str(input("会不会爆炸"))
    if next_3 == "不会":
        print("再检查检查")
    else:
        print("诶！ 自首了！抓起来抓起来")
else:
    print("下一个")
# 2.2.2 思考学校生活中有没有逻辑嵌套的场景，仿照 #2.2.1（变量赋值、打印等），实现代码逻辑
paper = int(input("我有几张打印纸？"))
if paper != 0 :
    paper_consume = int(input("我要打印几份啊"))
    if paper < paper_consume :
        print("还需要找""%d""份" % (paper_consume-paper))
    else:
        print("那没事了")
else:
    print("去找找")
# 2.2.3 人生的不同阶段：设置变量 age 的值，编写 if-elif-else 结构，根据 age 的值判断处于人生的哪个阶段
# 如果一个人的年龄小于 1 岁，就打印一条消息，指出他是婴儿
# 如果一个人的年龄为 1-2 岁，就打印一条消息，指出他是幼儿
# 如果一个人的年龄为 3-12 岁，就打印一条消息，指出他是儿童
# 如果一个人的年龄为 13-20 岁，就打印一条消息，指出他正处于青春期
# 如果一个人的年龄为 15-24 岁，就打印一条消息，指出他是年轻人
# 如果一个人的年龄为 18-64 岁，就打印一条消息，指出他是成年人
# 如果一个人的年龄超过 65 岁，就打印一条消息，指出他是老年人
age = int(input("你几岁啦"))
if age < 1 :
    print("婴儿")
elif age > 1 and age <=2:
    print("幼儿")
elif age >= 3 and age <=12:
    print("儿童")
elif age >= 13 and age <=20:
    print("正处于青春期")
elif age >= 15 and age <=24:
    print("年轻人")
elif age >= 18 and age <=64:
    print("成年人")
elif age > 65:
    print("老年人")