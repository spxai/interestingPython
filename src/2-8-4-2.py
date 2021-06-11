#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-4-2.py
import PySimpleGUI as sg     
import random as rnd
import time



guessNum=rnd.randint(1,100)
gameShowMess=["猜对了！","猜的数字大了","猜的数字小了"]
# 定义窗口内容
layout = [  [sg.Text("请输入您要机器猜的数字(1-100)")],     
            [sg.Input()],        
            [sg.Output(size=(40,2), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# 创建窗口
window = sg.Window('猜数字游戏', layout)      

minNum=1
maxNum=100

#显示和与窗口交互
while True:
    isGameContinue=True
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    playNum=int(values[0])
    gameState=guessNum-playNum
    while isGameContinue and playNum>=1 and  playNum<=100:  
        gameState=guessNum-playNum
        if gameState>0: 
            gameState=1
            maxNum=guessNum
            
        elif gameState<0:
            gameState=2  
            minNum=guessNum

        else:
            minNum=1
            maxNum=100  
            isGameContinue=False   
        window['-OUTPUT-'].update(window['-OUTPUT-'].Get()+'机器猜的数字是： ' + str(guessNum) + "!"+gameShowMess[gameState])
        guessNum=int((minNum+maxNum)/2)
               


#最后从屏幕上移除
window.close()                                 