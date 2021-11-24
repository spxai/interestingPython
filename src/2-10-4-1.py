#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-4-1.py

while True:   
    inputNum=input("请输入一个整数：")
    try:
        num=int(inputNum)
        print("输入正确！")
        break
    except:
        print("请输入正确的整数！")
        continue
