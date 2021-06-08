#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-3-1.py
import PySimpleGUI as sg                        # 第1部分-导入
# 定义窗口内容
layout = [  [sg.Text("hello,world")],     # 第2部分 - 指定层次（The Layout）
            [sg.Text("你好，世界")],
            [sg.Button('Ok')] ]
# 创建窗口
window = sg.Window('hello', layout)      # 第3部分-窗口定义

#显示和与窗口交互
event, values  = window.read()     # 第4部分-事件循环或调用window.read

#最后从屏幕上移除
window.close()                    # 第5部分-关闭窗口