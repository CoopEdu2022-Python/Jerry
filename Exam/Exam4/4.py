def add_(num1,num2):
    num1 , num2 =str(num1),str(num2)
    if num1.startswith("0") or num1.endswith("0") or num2.startswith("0") or num2.endswith("0"):
        print("输入数字不规范")
        return
    num1, num2 = float(num1), float(num2)
    answer = num1+num2
    print(round(answer,2))

add_("02342340","839023")
add_("2343523","34234.34324")
add_(str(input("随便输个数字吧")),str(input("随便输个数字吧")))