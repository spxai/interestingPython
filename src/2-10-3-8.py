#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-3-8.py
import base64
import random
import math
import json


fileName="2-10-3-8.7z"
logFileName="2-10-3-8.log"


with open(fileName,'rb') as fileObject:
    strTxt=fileObject.read()

logFile=open(logFileName,'w')


def printLog(*logStr):
    for data in logStr:
        logFile.write(str(data))
    logFile.write("\n\n")
    


def enCodeBase64(myStr):
    return base64.b64encode(myStr)

def deCodeBase64(myStr):
    return base64.b64decode(myStr)

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
        printLog("=")
        if (getGreatestCommonDivisor(i,x)==1):
            printLog(f">\n找到互质数:{i}")
            break
    return i  

def getModuloInverse(e,r):
    d=r-1
    for i in range(2,r):
        if i%100000==0: printLog(f"{i/r*100}%")
        if ((e*i)%r==1):
            d=i
            printLog("\n找到模逆元")
            break
    return d      
    
def getSegFromBytes(strTxt,maxMesLen,codeBase64=True):
    if codeBase64:
        encodeBytesStr=enCodeBase64(strTxt)
    else:
        encodeBytesStr=strTxt
    resultSegBytes=[len(encodeBytesStr)]
    for i in range(0,len(encodeBytesStr),maxMesLen):
        segBytes=encodeBytesStr[i:i+maxMesLen]
        resultSegBytes.append(int.from_bytes(segBytes,'little'))
    return resultSegBytes

def getBytesFromSeg(segBytes,maxMesLen,codeBase64=False):
    strBytes=[]
    strLen=segBytes[0]
    for data in segBytes[1:]:
        strBytes.append(data.to_bytes(length=maxMesLen,byteorder='little'))
    result=bytes.join(b"",strBytes)[0:strLen] 
    if codeBase64:
        result=deCodeBase64(result)
    return result


def encryptBytesList(segBytesList,e,N):
    encryedBytes=[]
    i=0
    bllen=len(segBytesList)
    encryedBytes.append(segBytesList[0])
    for data in segBytesList[1:]:
        i+=1
        if i% 500 ==0 :
            print(f"encrypt=>{i/bllen*100}%")
        encryedBytes.append(pow(data,e)% N)
    return encryedBytes
    
def decryptBytes(encryedSegBytesList,d,N):
    decryedBytes=[]
    i=0
    bllen=len(encryedSegBytesList)
    decryedBytes.append(encryedSegBytesList[0])
    for data in encryedSegBytesList[1:]:
        i+=1
        if i% 500 ==0 :
            print(f"decrypt=>{i/bllen*100}%")
        decryedBytes.append(pow(data,d)% N)
    return decryedBytes

def getJsonBytesFromSeg(strSeg,codeBase64=False):
    resultBytes=json.dumps(strSeg)
    if codeBase64:
        resultBytes=deCodeBase64(resultBytes)
    return resultBytes

def getSegFromJsonBytes(strBytes,codeBase64=True):
    if codeBase64:
        encodeBytesStr=enCodeBase64(strBytes)
    else:
        encodeBytesStr=strBytes
    resultSeg=json.loads(encodeBytesStr)
    return resultSeg


#p,q
minN=random.randint(10, 200) 
maxN=random.randint(minN+50, minN+100) 
p=getPrimeNumbers(minN,maxN)
minN=random.randint(200, 300) 
maxN=random.randint(minN+50, minN+100) 
q=getPrimeNumbers(minN,maxN)
printLog(f"p:{p},q:{q}")
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
printLog(f"\n公钥：({N},{e})\n私钥：({N},{d})")





lenN=len(str(N))
maxChar="~"#ascii=126
maxTestChar=""
segMessageLen=0
for i in range(1,lenN):
    maxTestChar+=maxChar
    if (int.from_bytes(bytes(maxTestChar,encoding='ascii'),'little')>N):
        segMessageLen=i-1
        break

    
printLog(N,maxTestChar,int.from_bytes(bytes("~"*segMessageLen,encoding='ascii'),'little'))    
printLog(strTxt) 

segBytesStrList=getSegFromBytes(strTxt,segMessageLen)
printLog(len(segBytesStrList),"segBytesStrList:",segBytesStrList)


encryptedMessList=encryptBytesList(segBytesStrList,e,N)
printLog(len(encryptedMessList),"encryptedMessList:",encryptedMessList)




encryptedFileName="2-10-3-8-7z-encry.dat"



encryptedFileJsonBytes=getJsonBytesFromSeg(encryptedMessList)
printLog(len(encryptedFileJsonBytes),encryptedFileJsonBytes)
tmp_decrySegBytesList=getSegFromJsonBytes(encryptedFileJsonBytes,False)
printLog(len(tmp_decrySegBytesList),"tmp_decrySegBytesList:",tmp_decrySegBytesList)



with open(encryptedFileName,'wb') as fileObject:
    fileObject.write(bytes(str(segMessageLen).encode('ascii')))
    fileObject.write(b'\x00'*20)
    fileObject.write(bytes(encryptedFileJsonBytes.encode("ascii")))

with open(encryptedFileName,'rb') as fileObject:
    encryptedFileCt=fileObject.read(100)
    printLog("head:",encryptedFileCt)
    encryptedsegMessageLen=0
    encryptedsegMessageLenI=0
    for i in range(0,len(encryptedFileCt)):
        if encryptedFileCt[i:i+20]==b'\x00'*20:
            encryptedsegMessageLen=int(encryptedFileCt[:i])
            encryptedsegMessageLenI=i
            break
    printLog(encryptedsegMessageLen)
    printLog(encryptedsegMessageLenI)
    fileObject.seek(encryptedsegMessageLenI+20)
    encryptedFileCt=fileObject.read().decode()
   
decrySegBytesList=getSegFromJsonBytes(encryptedFileCt,False)
printLog(len(decrySegBytesList),"decrySegBytesList:",decrySegBytesList)




decryptedMessList=decryptBytes(decrySegBytesList,d,N)
printLog(len(segBytesStrList),"segBytesStrList:",segBytesStrList)
printLog(len(decryptedMessList),"decryptedMessList:",decryptedMessList)
resStr=getBytesFromSeg(decryptedMessList,segMessageLen,True)
printLog(resStr)
printLog(strTxt) 


logFile.close()


with open(encryptedFileName+".7z",'wb') as fileObject:
    fileObject.write(resStr)