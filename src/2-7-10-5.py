#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-10-5.py

def swapNum(x,y):
    temp=x
    x=y
    y=temp
def swapNums(nums):
    temp=nums[0]
    nums[0]=nums[1]
    nums[1]=temp

x=11
y=22

swapNum(x,y)
print(x,y)
n=[11,22]
swapNums(n)
print(n)