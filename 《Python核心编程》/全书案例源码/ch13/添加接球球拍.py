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
ball_color = (255, 0, 0)  	#设置背景图片
ball_x = 10  				#弹球在x轴上的位置
ball_y = 10  				#弹球在y轴上的位置
   #调用弹球的颜色、位置、大小，并绘制到游戏窗口中
   game.draw.circle(game_window, ball_color, (ball_x, ball_y), 10)
paddle_color = (255, 140, 0) 				#设置球拍的颜色
mouse_x, mouse_y = game.mouse.get_pos()	#获取鼠标指针位置
#调用球拍的颜色、位置、大小，并绘制到游戏窗口中
game.draw.rect(game_window, paddle_color,(mouse_x, 470, 100, 10))