#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-4-6.py

while True:   
    inputNum=input("请输入一个整数：")
    try:
        num=int(inputNum)
    except BaseException as e:
        print(repr(e))
        print("请输入正确的整数！")
        continue
    else:
        print("输入正确！")
        break        
    finally:
        print("谢谢!")
