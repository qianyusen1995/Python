import pygame, sys   #导入Pygame和sys模块
pygame.init()                                        #初始化init()
screen = pygame.display.set_mode((500, 400))   #设置窗口大小
pygame.display.set_caption('我的第一个游戏：Hello Pygame!') #设置标题栏
while True:                                	#主程序循环体
     for event in pygame.event.get():
         if event.type == pygame.QUIT:  	#接收到退出事件后退出程序
             pygame.quit()
             sys.exit()
     pygame.display.update()            #刷新画面