#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-7-10.py

for x in range(2,101):
    for y in range(2,101):
        if (y % x ==0 and x!=y) or (x % y==0 and y!=x):
            print(x,y,end=",")
            
    
        
    