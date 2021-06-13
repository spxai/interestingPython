#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-10-7.py


def swapNums(nums):
    """
    swapNums函数接受一个列表对象，
    完成将列表对象的2个元素互换位置的功能。
    """    
    temp=nums[0]
    nums[0]=nums[1]
    nums[1]=temp

print(swapNums.__doc__)
print("---------------------")
help(swapNums)