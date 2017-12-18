#-*- coding:utf-8 -*-
import pygame
#导入pygame库
from sys import exit
#向sys模块接一个exit函数用来退出程序









pygame.init()
#初始化pygame，为使用硬件做准备
screen=pygame.display.set_mode((450,800),0,32)
#创建了一个窗口，窗口大小和背景图片大小一样
pygame.display.set_caption("Hello, world")
#设置窗口标题
background=pygame.image.load('bg.jpg').convert()
#加载并转换图像
plane=pygame.image.load('plane.png').convert()
#加载飞机图像
bullet=pygame.image.load('bullet.png').convert()
#加载子弹图像
bullet_x=0
bullet_y=-1
#初始化子弹位置
while True:
#游戏主循环
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			#接收到退出事件后退出程序
			pygame.quit()
			exit()
	screen.blit(background,(0,0))
	#将背景图画上去

	x,y=pygame.mouse.get_pos()
	#获取鼠标位置
	if bullet_y<0:
		#如果子弹超出了屏幕上端
		bullet_x=x-bullet.get_width()/2
		bullet_y=y-bullet.get_height()/2
		#把子弹的中心设置为鼠标坐标
	else:
		bullet_y-=5
		#子弹的位置往上移
	screen.blit(bullet,(bullet_x,bullet_y))
	#把子弹画在屏幕上
	x-=plane.get_width()/2
	y-=plane.get_height()/2
	#计算飞机左上角的位置
	screen.blit(plane,(x,y))
	pygame.display.update()
	#刷新一下画面