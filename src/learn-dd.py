#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from random import choice

ans = []
i=0
MaxNum=10000
MinNum=1
while i < 1000 :
    n1 = random.randint(MinNum,MaxNum)
    n2 = random.randint(MinNum,MaxNum) 
    print(f"第{i}题：{n1}+{n2} ,{n1}-{n2}" )
    ans.append((n1+n2,n1-n2))
    i += 1
print("*"*60)
i = 0
while i < len(ans):
    print(f"第{i}题的答案是：{ans[i]}")
    i += 1