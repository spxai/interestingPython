#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-4-2.py
class Teacher:
    name=""
    course=""
    def giveLessons(self,time,lessonsCount):
        print(self.name)
        print(self.course)
        print(time)
        print(lessonsCount)
        
myTeacher=Teacher()
myTeacher.name="张三"
myTeacher.course="数学"
myTeacher.giveLessons("周三、周五","2节课")