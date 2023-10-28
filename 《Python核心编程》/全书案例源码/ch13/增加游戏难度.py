speed_x = 1  #初始化游戏初速度x轴初始值
speed_y = 1  #初始化游戏初速度y轴初始值 
    #判断球拍接住弹球的位置区域
    elif mouse_x - 10 < ball_x < mouse_x + 110 and ball_y >= 460: 
        speed_y = -speed_y
        score += point
        count += 1       #成功接住一次弹球，次数+1
        if count == 5:  #判断球拍接住弹球超过5次，速度加快
            count = 0
            point += point
            if speed_x > 0:
                speed_x += 1
            else:
                speed_x -= 1
            speed_y -= 1 
score = 0 #设置计分器初始值
#获取计分器的值，并设置计分器文本颜色
my_sum = font.render(str(score), True, (255, 0, 0) , (255, 255, 255))
game_window.blit(my_sum, (60, 40)) #设置计分器的位置 
#判断球拍未接住弹球的位置区域
elif ball_y >= 490 and (ball_x <= mouse_x - 10 or ball_x >= mouse_x + 110):
        break
while True:
    background = pygame.image.load(background_image_filename).convert()
    for event in game.event.get():
        if event.type == game.QUIT:
            sys.exit()
    mouse_x, mouse_y = game.mouse.get_pos() #获取鼠标指针位置
    #调用弹球的颜色、位置、大小，并绘制到游戏窗口中
    game.draw.circle(game_window, ball_color, (ball_x, ball_y), 10) 
    #调用球拍的颜色、位置、大小，并绘制到游戏窗口中
    game.draw.rect(game_window, paddle_color,(mouse_x, 470, 100, 10)) 
    #获取计分器的值，并设置计分器文本颜色
    my_sum = font.render(str(score),True, (255, 0, 0),(255, 255,255)) 
    game_window.blit(my_sum, (60, 40)) #设置计分器的位置
    ball_x += speed_x
    ball_y += speed_y
    #判断弹球是否超过x轴的边界，是则反方向运动
    if ball_x <= 10 or ball_x >= 580: 
        speed_x = -speed_x
    if ball_y <= 10:
        speed_y = -speed_y
    #判断球拍接住弹球的位置区域
    elif mouse_x - 10 < ball_x < mouse_x + 110 and ball_y >= 460: 
        speed_y = -speed_y
        score += point
        count += 1
        if count == 5:
            count = 0
            point += point
            if speed_x > 0:
                speed_x += 1
            else:
                speed_x -= 1
            speed_y -= 1
#判断球拍未接住弹球的位置区域
elif ball_y >= 490 and (ball_x <= mouse_x - 10 or ball_x >= mouse_x + 110):
        break