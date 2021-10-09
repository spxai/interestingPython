#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-10-2-3.py
#待压缩字符串
my_str="""
If you do much work on computers, eventually you find that there’s some task you’d like to automate. For example, you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. 
"""
#码表
codeword_dictionary={}
#待压缩文本长度
str_len=len(my_str)
#码字最大长度
dict_maxlen=1
#将解析文本段的位置（下一次解析文本的起点）
now_index=0
#码表的最大索引
max_index=0

#
compressed_str=""

while (now_index<str_len):    
    #向后移动步长
    mystep=0
    #当前匹配长度
    now_len=dict_maxlen
    if now_len>str_len-now_index:
        now_len=str_len-now_index
    #查找到的码表索引，0表示没有找到
    cw_addr=0   
    while (now_len>0):
        cw_index=codeword_dictionary.get(my_str[now_index:now_index+now_len])
        if cw_index!=None:
            #找到码字
            cw_addr=cw_index
            mystep=now_len  
            break
        now_len-=1    
    if cw_addr==0:
        #没有找到码字,增加新的码字
        max_index+=1
        mystep=1
        codeword_dictionary[my_str[now_index:now_index+mystep]]=max_index
        print("没有找到码字,增加新的码字:{:s}，index:{:d}".format(my_str[now_index:now_index+mystep],max_index))
    else:
        #找到码字,增加新的码字
        max_index+=1    
        codeword_dictionary[my_str[now_index:now_index+mystep+1]]=max_index
        if mystep+1>dict_maxlen:
            dict_maxlen=mystep+1      
        print("找到码字:{:s},增加新的码字:{:s} ，index:{:d}".format(my_str[now_index:now_index+now_len],my_str[now_index:now_index+mystep+1],max_index))

    #计算压缩后结果
    cwdindex='%d'%cw_addr
    if cw_addr==0:
        cwlater=my_str[now_index:now_index+1] 
        now_index+=1
    else:
        now_index+=mystep     
        cwlater=my_str[now_index:now_index+1] 
        now_index+=1
    cw=cwdindex+cwlater
    compressed_str+=cw
print("\n------------------------------------\n")     
print(my_str)
print("\n************************************\n")
print(compressed_str)
print("\n------------------------------------\n")