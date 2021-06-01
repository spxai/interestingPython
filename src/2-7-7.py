#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-7.py
import turtle
turtle.color('Green','yellow')
while True:
    turtle.forward(200)
    turtle.left(150)
    print(turtle.pos())
    if abs(turtle.pos()) < 1:
        break
print('按回车键退出')
input()
