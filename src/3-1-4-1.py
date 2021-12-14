#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-4-1.py
import sys, pygame
import random
import time

pygame.init()
#sys.path[0]获取当前工作目录
pygame.display.set_caption("图片大小变更")
logo = pygame.image.load(sys.path[0]+r"\pic\3-1-4\game1.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load(sys.path[0]+r"\pic\3-1-4\bj.jpg")
bjpicRect = bjpic.get_rect()
bjpic=pygame.transform.scale(bjpic,(bjpicRect.width*0.6,bjpicRect.height*0.6))
size = width, height =bjpicRect.width*0.6,bjpicRect.height*0.6
screen = pygame.display.set_mode(size)
bjpic=pygame.Surface.convert(bjpic)
ball = pygame.image.load(sys.path[0]+r"\pic\3-1-4\game2.png")
ball=pygame.Surface.convert(ball)
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bjpic,(0,0)) 
    pygame.display.update()
    time.sleep(1)