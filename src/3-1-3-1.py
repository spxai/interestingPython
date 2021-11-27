#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-3-1.py
import sys, pygame
import random
import time

pygame.init()
#sys.path[0]获取当前工作目录
pygame.display.set_caption("图片大小变更")
logo = pygame.image.load(sys.path[0]+"/pic/3-1-1-1/ico.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load(sys.path[0]+"/pic/3-1-1-1/grounds.png")
bjpicRect = bjpic.get_rect()
size = width, height =bjpicRect.width*10,bjpicRect.height*10
screen = pygame.display.set_mode(size)
bjpic=pygame.Surface.convert(bjpic)
ball = pygame.image.load(sys.path[0]+"/pic/3-1-3/py.jpg")
ball=pygame.Surface.convert(ball)
ballrect = ball.get_rect()



bjpicWidth=bjpicRect.width
bjpicHeight=bjpicRect.height
nowX=0
nowY=0

newBallRectWidth=ballrect.width
newBallRectHeight=ballrect.height
i=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(10):
        nowX=i*bjpicWidth
        for j in range(10):
            nowY=j*bjpicHeight
            screen.blit(bjpic,(nowX,nowY)) 
     
    newBallRectWidth=(newBallRectWidth+10) % width   
    newBallRectHeight=(newBallRectHeight+10) % height
    print((newBallRectWidth,newBallRectHeight),width, height)
    newBall=pygame.transform.scale(ball,(newBallRectWidth,newBallRectHeight))
    screen.blit(newBall, (0,0))
    pygame.display.update()
    time.sleep(1)


    