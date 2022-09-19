# 3.1.2 电影票：编写一个循环，不断询问不同用户的年龄，并根据观众的年龄指出其票价
# 不到 3 岁的观众免费
# 3-12 岁的观众为 10 美元
# 超过 12 岁的观众为 15 美元

while 1:
    age = int(input("几岁啦:"))
    if age < 3:
        print("免费")
    elif age >= 3 and age < 12:
        print("10美元")
    elif age >12:
        print("15美元")

