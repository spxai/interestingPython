#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-3-4.py

def getGreatestCommonDivisor(a,b):
    while a != 0:
        a, b = b % a, a
    return b

print(getGreatestCommonDivisor(319,377))

