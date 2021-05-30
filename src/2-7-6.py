#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-6.py
import turtle

lineLen=90
ts = turtle.getscreen()
ts.colormode(255)
for b in range(0,256):
    turtle.color(0,0,b)
    turtle.fd(lineLen)
    posX,posY=turtle.position()
    turtle.goto(posX, posY+1)
    lineLen=-lineLen
ts.colormode(1)
print('按回车键退出')
input()