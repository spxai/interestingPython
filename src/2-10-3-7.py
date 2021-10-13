#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-3-7.py
import base64
import random
import math

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
    minN=random.randint(100,x)     
    for i in range(minN,x):
        print("=",end="")
        if (getGreatestCommonDivisor(i,x)==1):
            print(f">\n找到互质数:{i}")
            break
    return i  

def getModuloInverse(e,r):
    d=r-1
    for i in range(2,r):
        if i%100000==0: print(f"{i/r*100}%")
        if ((e*i)%r==1):
            d=i
            print("\n找到模逆元")
            break
    return d      
    
def getSegBytes(strTxt,maxMesLen):
    encodeBytesStr=enCodeBase64(strTxt)
    resultSegBytes=[len(encodeBytesStr)]
    for i in range(0,len(encodeBytesStr),maxMesLen):
        segBytes=encodeBytesStr[i:i+maxMesLen]
        resultSegBytes.append(int.from_bytes(segBytes,'little'))
    return resultSegBytes


def putSegBytes(segBytes,maxMesLen):
    strBytes=[]
    strLen=segBytes[0]
    for data in segBytes[1:]:
        strBytes.append(data.to_bytes(length=maxMesLen,byteorder='little'))
    
    return bytes.join(b"",strBytes)[0:strLen]    


def encryptBytes(segBytesList,e,N):
    encryedBytes=[]
    for data in segBytesList:
        encryedBytes.append(pow(data,e)% N)
    return encryedBytes
    
def decryptBytes(encryedSegBytesList,d,N):
    decryedBytes=[]
    for data in encryedSegBytesList:
        decryedBytes.append(pow(data,d)% N)
    return decryedBytes

#p,q
minN=random.randint(10, 200) 
maxN=random.randint(minN+50, minN+100) 
p=getPrimeNumbers(minN,maxN)
minN=random.randint(200, 300) 
maxN=random.randint(minN+50, minN+100) 
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


encodeStr=enCodeBase64(strTxt)


lenN=len(str(N))
maxChar="~"#ascii=126
maxTestChar=""
segMessageLen=0
for i in range(0,lenN):
    maxTestChar+=maxChar
    if (int.from_bytes(bytes(maxTestChar,encoding='ascii'),'little')>N):
        segMessageLen=i
        break
print(N,maxTestChar,int.from_bytes(bytes("~"*segMessageLen,encoding='ascii'),'little'))    
print(strTxt) 
print(encodeStr)
segBytesStr=getSegBytes(strTxt,segMessageLen)
print(segBytesStr)
encryptedMessList=encryptBytes(segBytesStr,e,N)
print(encryptedMessList)
decryptedMessList=decryptBytes(encryptedMessList,d,N)
print(decryptedMessList)
resStr=putSegBytes(decryptedMessList,segMessageLen)
print(resStr)
decodeDecryedStr=deCodeBase64(resStr)
print(decodeDecryedStr)
