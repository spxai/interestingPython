#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-10-1-1.py
fileName="2-10-1-1.txt"
print("文件内容:")
with open(fileName,encoding="utf8") as fileObject:
    fileTxts=fileObject.read()
print(fileTxts)