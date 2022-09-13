# # 1.3.1 完善课堂练习 1.2 中 #1.2.3~1.2.6 的输出语句，不要单独打印变量，而是打印一句完整的话。例如 #1.2.3 的输出为 “小明实际需要支付的金额是 xxx 元”
#
# # 1.3.2 开发一个计算圆的周长和面积的程序，用户输入圆的半径 r，在一行内打印圆的周长、面积，保留 2 位小数（π 取 3.14）
# r = float(input("请输入半径\n"))
# perimeter = float(2 * 3.14 * r)
# area = float(3.14 * r**2)
# print("周长为:" , "%.2f" %perimeter ,"\n", "面积为:" , "%.2f" %area ,sep="")
# # 1.3.3 开发一个简单的欢迎程序，新生输入自己的姓名和年级后，控制台会显示 “欢迎 xxx 开始 xx 年级的学习”
# name = str(input("请输入姓名\n"))
# grade = int(input("请输入年级\n"))
# print("欢迎",name,"开始",grade,"年级的学习", sep="")
# # 1.3.4 使用 input() 输入你的姓名、性别、学号，按照下方格式打印所有信息（左右对齐即可）
# name_1 = str(input("请输入姓名\n"))
# gender = str(input("您的性别是\n"))
# ID = str(input("您的student ID是\n"))
#
# print("---- info ----" , "\n" , "Name   : ", name_1 , "\n" , "Gender : ", grade , "\n" ,"ID     : " , ID, "\n","--------------",sep="")
# '''
# ---- info ----
# Name   :  Kros
# Gender :  male
# ID     :  0001
# --------------
# '''

# 1.3.5 赋值下列代码到文件，判断下列 4 个输出的结果（>>> 为输出），在每行 print 函数后，以注释的形式说明这行代码的效果，以及输出是否正确

print("%.2f" % 123.45678)  # ……
  # >>>  123.45
# 正确输出为 123.46  "%.2f" 意思为将”123.45678“转为浮点型小数后保留两位，进位错误
print("%.2f" % 123.4)
  # >>>  123.40
#正确输出为 123.40  "%.2f" 意思为将”123.4“转为浮点型小数后保留两位，正确。
print("%6.2f" % 1.2345)
  # >>>  1.23
#正确输出为”  1.23“  "%6.2f" 意思为将”1.2345“转为浮点型小数后保留两位且保持最小位数为6位。
print("%06.2f" % 1.2345)
  # >>>  1.23
#正确输出为”001.23“  "%06.2f" 意思为将”1.2345“转为浮点型小数后保留两位且保持最小位数为6位空余的部分用0填充。
print("%010.3f" % 3.1415926)
  #>>>  00000000003.142
#正确输出为”000003.142“  "%010.2f" 意思为将”3.1415926“转为浮点型小数后保留两位且保持最小位数为6位空余的部分用0填充。
# 1.3.6 打印两行数字，第 1 行为 8,9,10，第 2 行为 11,12,13，保证对齐
print(" " ,"8"," ",9," ",10, "\n", 11," ",12,"",13)
# 1.3.7 打印下方的五角星
print(" "*6, "*" , "\n", " "*5,"*"*3,"\n","*"*13,"\n"," "*3,"*"*7 ,"\n"," "*2,"*"*3, " "*3, "*"*3,"\n"," ","*"," "*9 ,"*",sep="")
'''
      *
     ***
*************
   *******
  ***   ***
 *         *
'''


# 1.3.8 创建 3 个变量，分别保存今天日期的年（2022）、月（9）、日（13），以 '-' 作为间隔符，使用 'today' 作为结束符，使用 print 函数打印出完整的日期
year = 2022
mouth = 9
day = 13
print(year,"-",mouth,"-",day,"today")