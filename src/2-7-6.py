#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-6.py
import turtle


ts = turtle.getscreen()
ts.colormode(255)
turtle.up()
turtle.goto(-300,-300)
turtle.down()
posX,posY=turtle.position()
turtle.pensize(2) 
for r in range(0,256,16):
    for g in range(0,256,16):
        for b in range(0,256,16):
            turtle.color(r,g,b)
            turtle.fd(6)            
        posY+=2
        posX=-300
        turtle.up()
        turtle.goto(posX,posY)
        turtle.down()        
ts.colormode(1)
print('按回车键退出')
input()