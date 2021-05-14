#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-1.py
import sys
import sys, pygame
pygame.init()
#sys.path[0]获取当前工作目录
logo = pygame.image.load(sys.path[0]+"/pic/3-1-1-1/ico.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load("H:/interestingPython/src/pic/3-1-1-1/grounds.png")
pygame.display.set_caption("我的第一个游戏")
bjpicRect = bjpic.get_rect()
 
size = width, height =bjpicRect.width*10,bjpicRect.height*10

screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bjpic, bjpicRect)
    pygame.display.flip()