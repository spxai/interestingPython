#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-5-1.py
import datetime
now=datetime.datetime.now()
name=input("输入名字:")
birthYear=input("您是哪一年出生的?")
age=now.year-int(birthYear)+1
print(f"{name},您今年虚岁:{age}")
