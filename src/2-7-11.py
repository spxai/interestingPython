#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-11.py
import turtle
turtle.color('Green','yellow')
turtle.home()
lineLine=100
for i in range((360//30)):
    turtle.setpos(0,0)
    turtle.forward(lineLine+i*10)
    turtle.left(30)  
    turtle.write(f"{i*30}>[{turtle.position()[0]},\n{turtle.position()[1]}]") 
turtle.home()
turtle.color('Black','red')
turtle.write(f"[{turtle.position()[0]},\n{turtle.position()[1]}]") 
turtle.color('Blue','red')

print('按回车键退出')
input()
