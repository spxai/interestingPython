#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-10-2-1.py
fileName="2-10-2-1.png"
print("文件内容:")
with open(fileName,'rb') as fileObject:
    fileTxts=fileObject.read()
    for data in fileTxts[:50]:
        print("%#x" % data,end=" ")