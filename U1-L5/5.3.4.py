# 5.3.4 下方是一个字典，记录了小明和小刚买水果的详细情况，为小明和小刚分别打印一条消息，描述他们买了哪些水果，花了多少钱
info = {
    '小明': {
        'fruits': ['苹果', '草莓', '香蕉'],
        'money': 89
    },
    '小刚': {
        'fruits': ['葡萄', '橘子', '樱桃'],
        'money': 87
    }
}

for _ in info.keys():
    print(_,end="")
    print("买了:",end=" ")
    print(info[_]["fruits"],end="")
    print("花费了",end="")
    print(info[_]["money"])
