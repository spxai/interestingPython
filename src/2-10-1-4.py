#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-10-1-4.py
fileName="2-10-1-4.txt"
print("文件内容:")
with open(fileName,'w',encoding="utf8") as fileObject:
    fileObject.write("Python提供了高效的高级数据结构，还能简单有效地面向对象编程\n")
    fileObject.write("Python提供了高效的高级数据结构，\n还能简单有效地面向对象编程\n")
    fileObject.write("Python提供了高效的高级数据结构，\n")
    fileObject.write("还能简单有效地面向对象编程\n")
with open(fileName,encoding="utf8") as fileObject:
    fileTxts=fileObject.read()
print(fileTxts)