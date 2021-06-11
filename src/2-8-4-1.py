#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-4-1.py
import PySimpleGUI as sg     
import random as rnd


playNum=rnd.randint(1,100)
gameShowMess=["猜对了，新的随机数已经重新生成！","您猜的数字大了","您猜的数字小了"]
# 定义窗口内容
layout = [  [sg.Text("计算机随机生成1-100以内的一个数字。\n请您猜测这个数字是多少?")],      
            [sg.Text("请输入您猜的数字")],     
            [sg.Input()],        
            [sg.Text(size=(40,2), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# 创建窗口
window = sg.Window('猜数字游戏', layout)      




#显示和与窗口交互
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    guessNum=int(values[0])
    gameState=guessNum-playNum
    if gameState>0: 
        gameState=1
    elif gameState<0:
        gameState=2  
    else:
        playNum=rnd.randint(1,100)
    window['-OUTPUT-'].update('你猜的数字是： ' + str(guessNum) + "!\n"+gameShowMess[gameState])

               

print(values[0])
#最后从屏幕上移除
window.close()                                 