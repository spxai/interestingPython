#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-3-2.py

def getPrimeNumbers(minNum,maxNum):
    pNs=[]
    import math
    for n in range(minNum,maxNum):
        for i in range(2,int(math.sqrt(n))+1): 
            if  (n%i==0):
                break            
        else:
            pNs.append(n)
    return pNs
            
pNums=getPrimeNumbers(3000,3500)
print(pNums)

