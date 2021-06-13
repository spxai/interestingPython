#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-11.py
import turtle
turtle.color('Green','yellow')
lineLine=50
for i in range(0,361,30):
    turtle.home()
    turtle.left(i)  
    turtle.forward(lineLine+i)  
    turtle.write(f"{i}>[{turtle.position()[0]},\n{turtle.position()[1]}]") 
turtle.home()
turtle.color('Black','red')
turtle.write(f"[{turtle.position()[0]},\n{turtle.position()[1]}]") 
turtle.color('Blue','red')

print('按回车键退出')
input()
