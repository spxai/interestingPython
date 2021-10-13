#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-3-5.py
import base64
import random

def enCodeBase64(myStr):
    return base64.b64encode(myStr.encode("utf8"))

def deCodeBase64(myStr):
    return base64.b64decode(myStr).decode("utf8")
 

strTxt="""
1978年出现了著名的RSA算法，它通常是先生成一对RSA密钥，
其中之一是保密密钥，由用户保存；
另一个为公开密钥，可对外公开，甚至可在网络服务器中注册。
为提高保密强度，RSA密钥至少为500位长，一般推荐使用1024位。
这就使加密的计算量很大。
"""

def getPrimeNumbers(minNum,maxNum):
    import math
    for n in range(minNum,maxNum):
        for i in range(2,int(math.sqrt(n))+1): 
            if  (n%i==0):
                break            
        else:
            pN=n
            break
    return pN

def getGreatestCommonDivisor(a,b):
    while a != 0:
        a, b = b % a, a
    return b

def getAnotherGcd(x):
    minN=random.randint(x-10000*10000, x-1)     
    for i in range(minN,x):
        print("=",end="")
        if (getGreatestCommonDivisor(i,x)==1):
            print(">\n找到互质数")
            break
    return i  

def getModuloInverse(e,r):
    d=r-1
    for i in range(2,r):
        if i%100000==0: print(".",end="")
        if ((e*i)%r==1):
            d=i
            print("\n找到模逆元")
            break
    return d      
    
    
    
#p,q
minN=random.randint(10010, 30000) 
maxN=random.randint(minN+10000, minN+20000) 
p=getPrimeNumbers(minN,maxN)
minN=random.randint(10010, 30000) 
maxN=random.randint(minN+1000, minN+2000) 
q=getPrimeNumbers(minN,maxN)
print(p,q)
#
N=p*q
#r
r=(p-1)*(q-1)
#e
e=getAnotherGcd(r)
#e关于r的模逆元d
d=getModuloInverse(e,r)
#公钥，私钥
pubKey=(N,e)
priKey=(N,d)
print(f"\n公钥：({N},{e})\n私钥：({N},{d})")



