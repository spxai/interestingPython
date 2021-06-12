#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-10-1.py


y=9
def getSum(x1,x2,x3,x4):
     global y    
     y=x1+x2+x3+x4
     return y

print(y)
print(getSum(11,22,33,44))
print(y)
