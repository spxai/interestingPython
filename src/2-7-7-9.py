#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-7-9.py
x=0
while x <20:
    if x >10:
        break
    print(x,end=" ")
    x+=1
print("\n------------------------")
for y in range(10):
    if y % 2 ==0:
        continue
    print(y,end=" ")
    
        
    