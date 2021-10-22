#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-9-2-1.py
import re
htmlStr="""
<html>
    <head>
         <meta charset="UTF-8"/>
         <title>Python3简介</title>
    </head>
    <body>
        <p>Python是一种广泛使用的解释型、高级和通用的编程语言。</p>
        <p>11.5+22.9=</p>
    </body>
</html>
"""
m=re.search(r'<title>(.*?)</title>',htmlStr)
htmlTitle=m.groups()[0]
print(f"标题：{htmlTitle}")
htmlBody=re.findall(r'<p>(.*?)</p>',htmlStr)
for htmlPCont in htmlBody:
    m=re.search(r'(\d+\.?\d+)(\D)(\d+\.?\d+)?(\D)',htmlPCont)
    if m:
        computeStrLst=m.groups()
        print(f"数字：{computeStrLst[0]}，{computeStrLst[2]}\n操作符：{computeStrLst[1]},{computeStrLst[3]}")
    else:    
        print(f"网页内容文本：{htmlPCont}")
    


