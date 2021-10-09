#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-10-1-2.py
fileName="2-10-1-1.txt"
print("文件内容:")
with open(fileName,encoding="utf8") as fileObject:
    for lineTxt in fileObject:
        print(lineTxt.rstrip())