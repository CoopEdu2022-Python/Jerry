# 1. 用多行注释的方式，写出 Python 目前所有的内置函数
dir(__builtins__)
#['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '
# __hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
# '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy',
# 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# 2. 用多行注释的方式，说明什么是公共方法；同时，用一些代码举几个简单的例子
"""公共方法指的是高级数据类型都可以使用的函数方法"""
a = "sdajbsdjbcxjkabcla"
print(max(a))
#x
# 3. 用多行注释的方式，简单描述公共方法和内置函数的关系
