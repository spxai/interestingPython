#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-12.py
import turtle
import math

def getFunY(a,b,c,x):
    y=a*x*x+b*x+c
    return y

x=-10
a=0.6
b=0.2
c=0.8
while x<=10:
    turtle.up()
    turtle.goto(x,getFunY(a,b,c,x))
    turtle.dot(2)
    x+=0.1
input()
