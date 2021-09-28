#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-4-3-Book.py
class Book:
    """书管理"""
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def getInfo(self):
        return f"书名:{self.name},作者:{self.author},价格:{self.price}"
        
        