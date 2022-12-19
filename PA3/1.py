import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控

# 内部各功能模块进行初始化创建及变量设置，默认调用
pygame.init()

# 设置游戏窗口大小，分别是宽度和高度
#size = width, height = 800, 600
window = pygame.display.set_mode((400,600))
# 初始化显示窗口

# 设置显示窗口的标题内容，str 类型
pygame.display.set_caption('hello world!')

my_font = pygame.font.SysFont("arial", 50)
text_surface = my_font.render("hello world!", True, (255, 225, 0))
window.blit(text_surface,(0,0))
pygame.display.flip()
# 无限循环，直到 Python 运行时退出结束
while True:
    # 从 Pygame 的事件队列中取出事件，并从队列中删除该事件
    for event in pygame.event.get():

        # 获得事件类型，并逐类响应
        if event.type == pygame.QUIT:
            # 用于退出结束游戏并退出
            exit()#这个前面的sys好像可以省是关键字吗？

    # 对显示窗口进行更新，默认窗口全部重绘
    pygame.display.update()