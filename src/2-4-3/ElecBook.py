#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-4-3-ElecBook.py
from Book import Book

class ElecBook(Book):
    """电子书管理"""
    def __init__(self,name,author,price,webName):
        super().__init__(name,author,price)
        self.webName="XX电子书超市"
        self.clickCount=0
    def getInfo(self):
        return f"书名:{self.name},作者:{self.author},价格:{self.price},售卖网站名:{self.webName},+点击次数{self.clickCount}"
    def clickBook(self):
        self.clickCount+=1
        