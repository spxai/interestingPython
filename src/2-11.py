#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-5.py
import json
students=[(1,28,'ζε'),(2,25,'ηδΊ')]  
print(students)
with open('stInfos.dat','w') as stFileObj:
    json.dump(students,stFileObj)
with open('stInfos.dat','r') as stFileObj:
    myStd=json.load(stFileObj)
    print(myStd)
    
  
    