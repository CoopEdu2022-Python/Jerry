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
    print("婴儿",end=" ")
elif age > 1 and age <=2:
    print("幼儿",end=" ")
elif age >= 3 and age <=12:
    print("儿童",end=" ")
if age >= 13 and age <=20:
    print("青春期",end=" ")
if age >= 15 and age <=24:
    print("年轻人",end=" ")
if age >= 18 and age <=64:
    print("成年人",end=" ")
elif age > 65:
    print("老年人")