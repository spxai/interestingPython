#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#8-1-3.py

import paddlehub as hub
lac = hub.Module(name="lac")
test_text =["北极光是由太阳风（逃离太阳的带电粒子）与地球的磁场和大气相互作用的结果。一般来说，极光常常出现于纬度靠近地磁极地区上空。"]
results=lac.lexical_analysis(texts = test_text)

print(results)