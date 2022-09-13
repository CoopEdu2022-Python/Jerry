# 1. 编写 4 个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字 8
anwser1_1 = 5 + 3  # 使用加法的例子
print(anwser1_1)

anwser1_2 = 4 + 4
anwser1_3 = 80/10
anwser1_4 = 2 * 4
anwser1_5 = 9 - 1
print(anwser1_2, anwser1_3, anwser1_4, anwser1_5 , sep="\n")
print(("**"+"分割线"+"**")*10)
# 2. 定义 2 个变量，使用任意 5 个不同的赋值运算符，打印 2 个变量的计算结果

anwser2_1 = 5
anwser2_1 += 3  # 使用 += 的例子
print(anwser2_1)
anwser2_2 = 1
anwser2_3 = 3
anwser2_2 += anwser2_3
anwser2_2 /= 2
anwser2_2 **= 9
anwser2_2 *= anwser2_3
anwser2_2 -= 100
print(anwser2_2, anwser2_3)

print(("**","分割线", "**"))
# 3. 小明想购买 1 台顶配的 iPhone 13 Pro Max，起售价为 12999 元，某店铺按 9.5 折出售，且提供每单 200 元的优惠券，小明实际需要支付的金额是？
print("3. 小明想购买 1 台顶配的 iPhone 13 Pro Max，起售价为 12999 元，某店铺按 9.5 折出售，且提供每单 200 元的优惠券，小明实际需要支付的金额是？")
iPhone_13 = 12999
now_iphone = (iPhone_13 * 0.95)-200
print(now_iphone)
print(("**"+"分割线"+"**")*10)
# 4. 小明有存款 56789 元，全部用于购买 #3 的 iPhone 13 Pro Max，最多能买多少台？
print("4. 小明有存款 56789 元，全部用于购买 #3 的 iPhone 13 Pro Max，最多能买多少台？")
allmoney_1 = 56789
number_phone = allmoney_1 // now_iphone
print(int(number_phone))
print(("**"+"分割线"+"**")*10)
# 5. 小红有存款 67890 元，全部用于购买 #3 的 iPhone 13 Pro Max，还能剩多少钱？
print("5. 小红有存款 67890 元，全部用于购买 #3 的 iPhone 13 Pro Max，还能剩多少钱？")
allmoney_2 = 67890
money_now = allmoney_2 % now_iphone
print("%.2f" % money_now)
print(("**"+"分割线"+"**")*10)
# 6. 小红把上述剩余的钱购买数字货币，每个月的收益为 +100%（每月翻一倍），一年后她有多少钱？
print("6. 小红把上述剩余的钱购买数字货币，每个月的收益为 +100%（每月翻一倍），一年后她有多少钱？")
rich = money_now * (2 ** 12)
print("%.2f" % rich)
# 7. 小红心里默念 50 次 “太棒了”。在控制台打印她的心理活动
print("7. 小红心里默念 50 次 “太棒了”。在控制台打印她的心理活动")
print("太棒了 " * 50)