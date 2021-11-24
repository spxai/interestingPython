#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-4-7.py
# 自定义异常类 
class InputOutRange(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

while True:   
    inputNum=input("请输入一个0-100的整数：")
    try:
        num=int(inputNum)
        if num>100 or num <0:
            raise InputOutRange(num)
    except ValueError:
        print("请输入整数！")
        continue
    except InputOutRange as e:
        print(f"{e.value}超过范围0-100")
        continue
    else:
        print("输入正确！")
        break        
    finally:
        print("谢谢!")
