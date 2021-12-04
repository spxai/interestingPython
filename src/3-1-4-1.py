#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-4-1.py
import sys, pygame
STARMAXHEALTH=100
BALLMAXHEALTH=100
class StartPlane:
    def __init__(self):
        self.img=pygame.image.load(sys.path[0]+"/pic/3-1-4/star.png")
        self.healthPoint=STARMAXHEALTH
        self.rect=self.img.get_rect()
        