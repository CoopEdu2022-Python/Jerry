# 20.1.1  Module & Package
# 1. 新建一个 equation 包
# 2. 在目录下，新建两个模块 conic 和 liner
# 3. 在 conic 模块中定义一个 Circle 类 和 Ellipse 类，Circle 继承自 Ellipse
# 4. 在 Circle 类中定义 perimeter 方法和 area 方法
# 5. 在 receive_message 文件中定义一个 receive 函数
# 6. 新建 test.py，直接导入 equation 包

# ---
# 20.1.2  Python 依赖管理  [50pts]
# 通过搜索引擎了解以下问题：
# 1. Python 依赖是什么？
# 一个插件要正常运行,需要的另一个程序
# 2. Python 的依赖管理存在哪些问题？
"""不同版本依赖切换麻烦
项目环境混乱"""
# 3. Dependency hell 是什么？
"""在操作系统中由于软件之间的依赖性不能被满足而引发的问题"""
# 4. 为什么会出现这些问题？
"""Python版本迭代快，依赖的包不适用"""
# 5. Python 是如何解决这些问题的？
"""搭建虚拟环境以及第三方管理"""
# 6. 是否有第三方工具解决了这些问题？
"""pip
能快速配置好项目依赖，搭建好开发环境。
明确知道当前项目依赖了哪些第三方的包，以及他们的依赖树。
能快速添加和移除给定的依赖，进行依赖调解。
Conda……https://cloud.tencent.com/developer/article/2135411"""