#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-10-6.py

def swapNums(nums):
    temp=nums[0]
    nums[0]=nums[1]
    nums[1]=temp

swap=swapNums
n=[11,22]
print(n)
swap(n)
print(n)