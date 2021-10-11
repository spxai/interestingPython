#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#2-5-6.py
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
print(queue.popleft())
queue.append(3)
print(queue.popleft())
queue.append(4)
queue.append(5)
print(queue.popleft())
print(queue)
for data in queue:
    print(data)
