#导入游戏所需模块
import pygame
import pygame as game
import sys
import random
import time

#程序初始化及基本参数设置
game.init()
game_window = game.display.set_mode((600, 500)) 	#设置游戏窗口大小
game.display.set_caption('接弹球计分游戏') 			#设置游戏标题名称
while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            sys.exit()
    game.display.update()  #程序刷新，重新绘制游戏状态
background_image_filename = 'bj.jpg'  		#设置背景图片
   background = pygame.image.load(background_image_filename).convert()
   game_window.blit(background, (0, 0)) 	#写入背景图片