#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-9-2-2.py
import re
def updateStack(computeStr,s1,s2,opsPriority):
    m=re.search(r'^(\D+?)',computeStr)    
    strType=''
    if m:
        strType='operator'
    else:
        m=re.search(r'^(\d*\.?\d*)',computeStr)
        strType='num'
        

    splitWord=m.groups()
    if strType=='operator':
        if len(splitWord[0])>0:
            operator=splitWord[0]
            if operator not in ('(',')'):
                while len(s1)>0:
                    if opsPriority[s1[-1]]<opsPriority[operator]:
                        s1.append(operator)
                        break
                    else:
                        s2.append(s1.pop())
            elif operator=='(':
                s1.append(operator)
            elif operator==')':
                while len(s1)>0:
                    getOpt=s1.pop()
                    if getOpt=='(':
                        break
                    else:
                        s2.append(getOpt)
    else:
        s2.append(float(splitWord[0]))
    return (m.start(),m.end())
 
def clearStack(s1,s2):
    while len(s1)>1:
        s2.append(s1.pop())
             

center_computer=[r"11+3*7-9/3",r"(1+3)*(1+9)+16/(4*2)",r"(11+32.61)/8*66/6",r"(11+32.61)/(8*66)"]
operatorsPriority={'#':0,'+':1,'-':1,'*':2,'/':2,'(':0,')':0}

for cpStr in center_computer:
    tempStack=['#']
    resStack=[]
    comptingStr=cpStr.replace(" ","")
    print(comptingStr)
    while len(comptingStr)>0:
        tokenInfo=updateStack(comptingStr,tempStack,resStack,operatorsPriority)
        comptingStr=comptingStr[tokenInfo[1]:]
    clearStack(tempStack,resStack)
    resStack.reverse()  
    print(resStack)