# 4.2.2 编写一个名为 make_shirt() 的函数，用户输入尺码以及要印到短袖上的文字。这个函数应打印一个句子，告知用户短袖的尺码和文字，便于用户确认
def chengshan():
    juzi = str(input("需要印刷啥"))
    size = int(input("你要几号的衣服"))
    print("用户尺码为", size,"在衣服上印刷句子：",juzi)
chengshan()