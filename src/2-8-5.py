#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-4-2.py
import PySimpleGUI as sg     
import random as rnd
import time
from enum import Enum


playerNums=[]
playerNumSum=0
computerNums=[]
computerNumSum=0
computerWin=False
playerWin=False
GamePlayer=Enum('GamePlayer', 'COMPUTER PLAYER')
gameShowMess=["玩家停止抽数！","玩家继续抽数：","电脑停止抽数","电脑继续抽数："]

def updateStatus(statusStr,window):
    window['-OUTPUT-'].update(statusStr+ "\n"+window['-OUTPUT-'].Get())
    
def AddRndNum(gamePlayer):
    global  playerNumSum,computerNumSum
    if gamePlayer==GamePlayer.COMPUTER:
        computerNum=rnd.randint(1,10)
        computerNums.append(computerNum)  
        computerNumSum+=computerNum
        return computerNum   
    else:            
        playerNum=rnd.randint(1,10)
        playerNums.append(playerNum)
        playerNumSum+=playerNum
        return playerNum

def AddPlayerNum(window):
    nRes=AddRndNum(GamePlayer.PLAYER)
    updateStatus(gameShowMess[1] + str(nRes) + "!总点数:"+ str(GetPlayerSum()),window) 
    return GetPlayerSum()
    
    
def AddComputerNum(window):
    nRes=AddRndNum(GamePlayer.COMPUTER)
    updateStatus(gameShowMess[3] + str(nRes) + "!总点数:"+ str(GetComputerSum()),window) 
    return GetComputerSum()
    
def GetPlayerSum():
    return playerNumSum
def GetComputerSum():
    return computerNumSum
    
def UpdateIsGameOver(gamePlayer):
    computerWin=playerWin=False
    if gamePlayer==GamePlayer.COMPUTER and GetPlayerSum()>21:
        computerWin=False
        playerWin=True           
    if gamePlayer==GamePlayer.PLAYER and GetComputerSum()>21:
        computerWin=True
        playerWin=False    
    return (computerWin,playerWin)

def main():   

    # 定义窗口内容
    layout = [  [sg.Text("您是否继续抽数？")],            
                [sg.Button('Yes'), sg.Button('No'),sg.Button('Exit')],
                [sg.Output(size=(40,2), key='-OUTPUT-')]]
    
    # 创建窗口
    window = sg.Window('21点游戏', layout)      
    

    #显示和与窗口交互
    while True:
        isComputerContinue=True
        isPlayerContinue=True
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit': 
            break
        if isPlayerContinue: 
            if event == 'Yes':
                updateStatus("玩家确定抽数",window)
            elif event == 'No':
                updateStatus("玩家放弃抽数",window)  
                isPlayerContinue=False      
        else:
            updateStatus("玩家放弃抽数",window)   
        if isComputerContinue :
            updateStatus("电脑确定抽数",window) 
        else:
            updateStatus("电脑放弃抽数",window)            
            
        if isPlayerContinue:  
            AddPlayerNum(window)
            (cWin,pWin)=UpdateIsGameOver(GamePlayer.PLAYER)  
            if pWin:
                updateStatus("玩家赢了",window)  
                break
            elif cWin:
                updateStatus("电脑赢了",window)   
                break
        if isComputerContinue :
            AddComputerNum(window)
            (cWin,pWin)=UpdateIsGameOver(GamePlayer.COMPUTER)
            if pWin:
                updateStatus("玩家赢了",window)  
                break
            elif cWin:
                updateStatus("电脑赢了",window)   
                break

  


                
    
    
    #最后从屏幕上移除
    window.close()   

if __name__ == "__main__":
    main()
    exit()