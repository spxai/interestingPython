#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def __updateStack(computeStr,s1,s2,opsPriority):
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
 
def __clearStack(s1,s2):
    while len(s1)>1:
        s2.append(s1.pop())
             



def getResultFromStr(cpStr):   
    operatorsPriority={'#':0,'+':1,'-':1,'*':2,'/':2,'(':0,')':0}
    tempStack=['#']
    resStack=[]
    comptingStr=cpStr.replace(" ","")

    while len(comptingStr)>0:
        tokenInfo=__updateStack(comptingStr,tempStack,resStack,operatorsPriority)
        comptingStr=comptingStr[tokenInfo[1]:]
    __clearStack(tempStack,resStack)
    resStack.reverse()  

    
    #----逆波兰表达式求解
    opts=operatorsPriority.keys()
    runStack=[]
    while  len(resStack)>0:
        data=resStack.pop()
        if data not in opts:
            runStack.append(data)
        else:
            n2=runStack.pop()
            n1=runStack.pop()
            result=eval(str(n1)+data+str(n2))
            runStack.append(result)

    return runStack[0]

    
    
    




