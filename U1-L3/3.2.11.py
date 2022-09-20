# 3.1.11 制作一个动态的进度条（提示：使用 print 函数的 end 参数）
import time
for i in range(1,300,1):
    print("!!!!",end="")
    time.sleep(1)

