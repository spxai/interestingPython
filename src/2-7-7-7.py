#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-7-7-7.py
x=int(input("请输入一个数:"))
if x % 2 ==0:
    print("x可以被2整除")
    if x%3 ==0:
        print("x可以被3整除")
    else:
        print("x不能被3整除")