#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-2-2.py
import sys, pygame
import random

pygame.init()
#sys.path[0]获取当前工作目录
pygame.display.set_caption("我的第一个游戏")
logo = pygame.image.load(sys.path[0]+"/pic/3-1-1-1/ico.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load(sys.path[0]+"/pic/3-1-1-1/grounds.png")
bjpicRect = bjpic.get_rect()
size = width, height =bjpicRect .width*15,bjpicRect .height*15
ball = pygame.image.load(sys.path[0]+"/pic/3-1-2/intro_ball.gif")
ballrect = ball.get_rect()

screen = pygame.display.set_mode(size)
bjpicWidth=bjpicRect .width
bjpicHeight=bjpicRect .height
nowX=0
nowY=0

speed = [random.randint(5,10), random.randint(5,10)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(15):
        nowX=i*bjpicWidth
        for j in range(15):
            nowY=j*bjpicHeight
            screen.blit(bjpic,(nowX,nowY))
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        speed
    screen.blit(ball, ballrect)
    pygame.display.flip()


    