#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-4-2.py
import PySimpleGUI as sg     
import random as rnd
import time



guessNum=rnd.randint(1,100)
gameShowMess=["玩家停止抽数！","玩家继续抽数：","电脑停止抽数","电脑抽数："]
# 定义窗口内容
layout = [  [sg.Text("您是否继续抽数？")],            
            [sg.Button('Yes'), sg.Button('No'),sg.Button('Cancel')],
            [sg.Output(size=(40,2), key='-OUTPUT-')]]

# 创建窗口
window = sg.Window('21点游戏', layout)      

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