#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-3-6.py
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
maxMesLen=5
def getSegBytes(strTxt):
    encodeBytesStr=enCodeBase64(strTxt)
    resultSegBytes=[len(encodeBytesStr)]
    for i in range(0,len(encodeBytesStr),maxMesLen):
        segBytes=encodeBytesStr[i:i+maxMesLen]
        resultSegBytes.append(int.from_bytes(segBytes,'little'))
    return resultSegBytes


def putSegBytes(segBytes):
    strBytes=[]
    strLen=segBytes[0]
    for data in segBytes[1:]:
        strBytes.append(data.to_bytes(length=maxMesLen,byteorder='little'))
    return bytes.join(b"",strBytes)[0:strLen]

print(strTxt)
print(enCodeBase64(strTxt))
segBytesStr=getSegBytes(strTxt)
print(segBytesStr)
resStr=putSegBytes(segBytesStr)
print(resStr)
print(deCodeBase64(resStr))