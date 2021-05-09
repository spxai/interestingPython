#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-3-2-8.py
import random
import os
x=random.randint(5,10)
print(x)
print(os.urandom(10))
random.seed(os.urandom(10))
x=random.randint(5,10)
print(x)
random.seed()
x=random.randint(5,10)
print(x)