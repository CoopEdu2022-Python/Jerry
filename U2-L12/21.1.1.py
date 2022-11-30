# 使用 open() 函数打开文件并读取文件中的内容时，总是会从文件的第一个字符（字节）开始读起。那么，有没有办法可以指定读取的起始位置呢？
# 借助搜索引擎查询解决方案，配合代码体现成果
"""whence：作为可选参数，用于指定文件指针要放置的位置，该参数的参数值有 3 个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。
offset：表示相对于 whence 位置文件指针的偏移量，正数表示向后偏移，负数表示向前偏移。例如，当whence == 0 &&offset == 3（即 seek(3,0) ），表示文件指针移动至距离文件开头处 3 个字符的位置；当whence == 1 &&offset == 5（即 seek(5,1) ），表示文件指针向后移动，移动至距离当前位置 5 个字符处。
————————————————
原文链接：https://blog.csdn.net/qq_39935684/article/details/120752725"""
file = open("text.1",mode="r+",encoding="utf-8")
file.seek(5,0)
file.write("A")
file.close()