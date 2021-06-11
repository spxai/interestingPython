#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-7-11.py

for x in range(2,101):
    for y in range(2,101):        
        if ((x+y) % x ==0 or (x+y) % y ==0 )and not(x==y) :
            print(x,y,end=",")
            
    
        
    