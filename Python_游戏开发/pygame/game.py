# encoding=utf-8

# 字符串
a = "1_jeff"
b = "2_jeff"
c = "3_jeff"
print('分别输出 a b c 的值：', a, b, c)

# 变量运算
a = "11"
b = "2"
c = "31"
print(a + b)
print(a + b)
print(a + c)

# if语句
a = '11'
if a == 11:
    print("a是等于11")
elif a == 2:
    print("a是等于2")
elif a == 3:
    print("a是等于3")
else:
    print("判断错误")

# if语句嵌套
a = 2
b = 3
if a == 2:
    if b == 3:
        print("完全符合要求")
else:
    print("第一项要求都没符合耶")

# while语句
i = 0
while i < 3:
    print("你好")
    i = i + 1

# 列表for循环
a = [99, 6, 7, 85, 2, 3]
for v in a:
    print(v)


# 自定义函数
def abc(a, b):
    return a + b


c = abc(1, 2)
print(c)


# 类和对象
class human:
    name = ""
    age = 0

    def say(self):  # say是方法； self当前这个类型之中
        print("hello")

    def myInfo(self):
        print("myName:", self.name, "myAge:", self.age)


xiaoM = human()
xiaoM.say()
xiaoM.myInfo()
xiaoM.name = "XiaoMing"
xiaoM.age = 18
xiaoM.myInfo()

'''做游戏'''
# 导入pygame
import pygame, random

'''游戏素材添加'''
bg = pygame.image.load(r'E:\2dsrc\src\img\bg.png')
hero = pygame.image.load(r'E:\2dsrc\src\img\hero1.png')
enemy = pygame.image.load(r'E:\2dsrc\src\img\enemy1.png')
enemy_boom = pygame.image.load(r'E:\2dsrc\src\img\enemy1_down1.png')
bullet = pygame.image.load(r'E:\2dsrc\src\img\bullet1.png')  # 一个是背景图、一个是主角图、一个是敌人图、一个是敌人被击中后的爆炸图、一个是子弹图片

'''游戏初始化'''
pygame.init()
screen = pygame.display.set_mode((600, 800))  # display 有一个g功能就是创建窗口，名叫 set_mode，我们在 set_mode 中传入这个屏幕的宽高
pygame.display.set_caption("这是一个Jeff的飞机游戏")

heroX = 250
heroY = 680
stepX = 0  # 用来检测用户是否按下了上下左右。
stepY = 0  # 用来检测用户是否按下了上下左右。

bullets_pos = []  # 子弹位置
enemy_speed = 2  # 敌机速度为5
enemy_objs = []  # 列表用来记录创建的敌人对象
enemy_objs1 = []
enemy_objs2 = []
enemy_objs3 = []
bullets_pos = []
bullet_speed = []

'''增加敌机'''
def enemy_show(enemy_objs, startY=-40):  # enemy_show方法：（enemy_objs列表:用来记录创建的敌人对象,startY：默认的 Y 坐标）
    if len(enemy_objs) < 5:  # 如果敌机数量小于 5 个
        while len(enemy_objs) < 5:  # 使用 while 循环进行创建
            enemy_X = random.randint(0, 500)  # 产生 0 到 500 的一个整数型随机数
            enemy_pos = [enemy_X, startY]  # 把创建对象的 X 和 Y 值（enemy_pos 即敌机位置）存储到
            # enemy_objs 列表中
            screen.blit(enemy, enemy_pos)  # blit 的第1个参数是图片参数，第2个参数是整个屏幕的 x 和 y 坐标，也就是从哪里开始画；x 越大越靠右，y 越大越靠下。
            enemy_objs.append(enemy_pos)  # 把创建的敌机对象的 X 和 Y 值存储到 enemy_objs 列表中
    else:
        i = 0
        for pos in enemy_objs:
            screen.blit(enemy, pos)
            enemy_objs[i] = [pos[0], pos[1] + enemy_speed]  # y 轴坐标的增加
            i = i + 1
    return enemy_objs

'''屏幕边界'''
def screen_border(X,Y):
    #左右屏幕
    if X<0:
        X=0
    elif X>500:
        X=500
    #上下屏幕
    if Y<0:
        Y=0
    elif Y>700:
        Y=700
    return X,Y

'''距离'''
def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a*a+b*b)

'''控制主角飞机移动'''
# keydown_envent方法：用来检测按下按钮event(事件）后的处理
def keydown_event(event, stepX, stepY,hero_pos):
    bullet_pos = []
    if event.key == pygame.K_RIGHT:
        stepX = 5
    elif event.key == pygame.K_LEFT:
        stepX = -5
    elif event.key == pygame.K_UP:
        stepY = -5
    elif event.key == pygame.K_DOWN:
        stepY = 5
    elif event.key == pygame.K_SPACE:  # 在event响应按键方法中添加空格K_SPACE事件的响应，
        bullet_pos = [hero_pos[0], hero_pos[1] + 10]  # 绘制出一个子弹
    return stepX, stepY,bullet_pos

'''游戏主循环'''
while True:
    bullet_pos = []
    # 控制主角飞机移动
    heroX = heroX + stepX
    heroY = heroY + stepY

    # blit方法是screen 的功能之一，也就是可以在屏幕中画出我们加载的图片；blit 的第一个参数是图片参数，第二个参数是整个屏幕的 x 和
    # y 坐标，也就是从哪里开始画；x 越大越靠右
    screen.blit(bg, (0, 0))
    screen.blit(hero, (heroX, heroY))
    enemy_objs = enemy_show(enemy_objs)
    #enemy_objs1=enemy_show(enemy_objs1,-300)
    #enemy_objs2=enemy_show(enemy_objs2,-600)
    #enemy_objs3=enemy_show(enemy_objs3,-900)
    print(bullets_pos)

    # 子弹
    i = 0
    # 判断 bullet_pos 接收值后长度是否大于 1，大于则表示已经按下空格，则记录在 bullets_pos
    # 列表中；之后使用循环遍历每个子弹的位置，然后在 Y 轴上减去一个值即可发射子弹。
    for v in bullets_pos:  # 此部分新增
        bullets_pos[i] = [v[0], v[1] - 10] # 在 Y 轴上减去一个值即可发射子弹。
        screen.blit(bullet, (bullets_pos[i][0] + 45, bullets_pos[i][1])) # 飞机会占据一定宽度，+45 是为了保持子弹在飞机头位置中间进行发射。
        distance_b = [bullets_pos[i][0] + 45, bullets_pos[i][1]]
        # 在子弹移动时添加距离计算，如果子弹移动后与敌机小于一定距离，那么就在敌机位置显示出爆炸图片就可以了。
        ei = 0
        for ep in enemy_objs:
            if distance(distance_b[0], distance_b[1], ep[0], ep[1]) < 60: # 如果距离达到了我们就在那个位置
                print('\n\n\n\n\n\n\n\n\n\n\n\n boom')
                screen.blit(enemy_boom, (ep[0], ep[1])) # 显示爆炸图片
                enemy_objs[ei] = [random.randint(0, 500), -50] # 并且更改这个位置到初始位置重新掉落。
            ei = ei + 1
        i = i + 1

    # 游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 用if判断event的类型如是pygame游戏中的QUIT
            # ，那么就执行exit()
            exit()

        if event.type == pygame.KEYDOWN:  # while循环中：e.g.如果是K_RIGHT(
            # 右键）那么就增加下次绘制图片的 x 坐标值依次类推
            stepX, stepY = keydown_event(event, stepX, stepY)
    pygame.display.update()  # 循环完我们都需要刷新整个界面，否则是不会呈现画完的效果的