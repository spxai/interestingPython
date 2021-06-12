#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-10-4.py


def printY():
     y=9
     print(y)
     def getSum(x1,x2,x3,x4):
          nonlocal y    
          y=x1+x2+x3+x4
     getSum(100,2,3,4)
     print(y)
     
printY()
