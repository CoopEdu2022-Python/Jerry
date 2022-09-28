# 5.2.4 定义一个元祖类型的购物车，用户可以不断的输入想添加的商品，输入 'q' 结束，打印出当前购物车中商品的数量，以及所有的商品
def market_plan():
    plan_list = []
    while 1:
        plan = input()
        if plan != "q" :
            plan_list.append(plan)
        else:
            rtx = (plan_list, )
            return rtx
def true_print(a):
    for i in range(0, len(a)):
        print(a[i], end=" ")
    print("列表中有：",len(a),"个")
    print(type(a))
true_print(market_plan())
