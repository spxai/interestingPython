#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#testModule262.py
def sumN(n):
    sum=0
    for i in range(n):
        sum+=i
    return sum

def printSum(n):
    sum=0
    for i in range(1,n):
        sum+=i
        print(i," sum:",sum)    

def main():
    print(sumN(6))


if __name__ == "__main__":
    main()
    exit()

print(__name__)
printSum(6)
