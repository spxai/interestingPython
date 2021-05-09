#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-3-2-4.py
import random
xbytes=random.randbytes(10)
for i in xbytes:
    print("%x"%i,end=",")
print("")
xbytes=random.randbytes(2)
for i in xbytes:
    print("%x"%i,end=",")