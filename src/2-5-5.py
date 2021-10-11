#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-5-5.py
def printStack(stackData):
    print("-----")
    for data in stackData:
        print(data)
    print("-----")
stack=[]
stack.append(1)
printStack(stack)
stack.append(2)
printStack(stack)
stack.append(3)
printStack(stack)
data=stack.pop()
print(f"pop:{data}")
printStack(stack)
data=stack.pop()
print(f"pop:{data}")
printStack(stack)
