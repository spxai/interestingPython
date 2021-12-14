#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-4-1.py
import sys, pygame
import random
import time

pygame.init()
#sys.path[0]获取当前工作目录
pygame.display.set_caption("图片大小变更")
logo = pygame.image.load(sys.path[0]+"/pic/3-1-4-1/game1.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load(sys.path[0]+"/pic/3-1-4-1/grounds.png")
bjpicRect = bjpic.get_rect()
size = width, height =bjpicRect.width*10,bjpicRect.height*10
screen = pygame.display.set_mode(size)
bjpic=pygame.Surface.convert(bjpic)
ball = pygame.image.load(sys.path[0]+"/pic/3-1-4-1/game2.png")
ball=pygame.Surface.convert(ball)
ballrect = ball.get_rect()
        