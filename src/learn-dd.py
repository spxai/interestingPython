#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#自动生成速算题
import random


#加减法
question = []
i=0
MaxNum=10000
MinNum=1
while i < 1000 :
    n1 = random.randint(MinNum,MaxNum)
    n2 = random.randint(MinNum,MaxNum) 
    question.append((f"{n1}+{n2}",n1+n2))
    question.append((f"{n1}-{n2}",n1-n2))
    i += 2
    print("*",end="")



#乘法

i=0
MaxNum=1000
MinNum=1

while i < 1000 :
    n1 = random.randint(MinNum,MaxNum)
    n2 = random.randint(MinNum,MaxNum) 
    question.append((f"{n1}×{n2}",n1*n2))
    i += 1
    print("*",end="")
    
    
#除法
i=0
MaxNum=10000
MinNum=2  
#合数是指在大于1的整数中除了能被1和本身整除外，还能被其他数（0除外）整除的数。
nonPrimeNums=[(x,int(y/x),y) for y in range(MinNum,MaxNum) for x in range(2,y) if y%x==0]
timu=[]
for n1,n2,nonPrimeNumber in nonPrimeNums:
    timu.append((f"{nonPrimeNumber}÷{n1}",n2))
question=question+random.sample(timu,1000)  
    
print()
exerciseQuestion=random.sample(question,250)   
i = 0
while i < len(exerciseQuestion):
    print(f"第{i}题{exerciseQuestion[i][0]}")
    i += 1

i = 0
while i < len(exerciseQuestion):
    print(f"第{i}题的答案是：{exerciseQuestion[i][1]}")
    i += 1
