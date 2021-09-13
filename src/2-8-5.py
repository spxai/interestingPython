#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-4-2.py
import PySimpleGUI as sg     
import random as rnd
import time


playerNums=[]
playerNumSum=0
computerNums=[]
computerNumSum=0
computerWin=False
playerWin=False
GamePlayer=Enum('GamePlayer', 'COMPUTER PLAYER')

def UpdateStatus(statusStr,window):
    window['-OUTPUT-'].update(window['-OUTPUT-'].Get()+ statusStr+"\n")
    
def AddRndNum(gamePlayer):
    if gamePlayer==GamePlayer.COMPUTER:
        computerNum=rnd.randint(1,10)
        computerNums.append(computerNum)  
        computerNumSum+=computerNum
        return computerNum       
    else:            
        playNum=rnd.randint(1,10)
        playerNums.append(playNum)
        playerNumSum+=playNum
        return playerNum

def AddPlayerNum():
    rndNum=AddRndNum(GamePlayer.PLAYER)
    UpdateStatus(gameShowMess[1] + str(rndNum) + "!" ,window) 
    return GetPlayerSum()
    
    
def AddComputerNum():
    rndNum=AddRndNum(GamePlayer.COMPUTER)
    UpdateStatus(gameShowMess[3] + str(rndNum) + "!" ,window) 
    return GetComputerSum()
    
def GetPlayerSum():
    return playerNumSum
def GetComputerSum():
    return computerNumSum
    
def UpdateIsGameOver(gamePlayer,numSum):
    if gamePlayer==GamePlayer.COMPUTER and numSum>21:
        computerWin=False
        playerWin=True           
    if gamePlayer==GamePlayer.PLAYER and numSum>21:
        computerWin=True
        playerWin=False    
    return (computerWin,playerWin)

def main():   
    gameShowMess=["玩家停止抽数！","玩家继续抽数：","电脑停止抽数","电脑继续抽数："]
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
                UpdateStatus("玩家确定抽数",window)
            elif event == 'No':
                UpdateStatus("玩家放弃抽数",window)  
                isPlayerContinue=False      
        else:
            updateStatus("玩家放弃抽数",window)   
        if isComputerContinue :
            updateStatus("电脑确定抽数",window) 
        else:
            updateStatus("电脑放弃抽数",window)            
            
        if isPlayerContinue:  
            (cWin,pWin)=UpdateIsGameOver(GamePlayer.PLAYER,AddPlayerNum())  
        if isComputerContinue :
            (cWin,pWin)=UpdateIsGameOver(GamePlayer.COMPUTER,AddComputerNum())
        if cWin or pWin:
            #有一方赢了，游戏结束
        else:
            #游戏没有结束，继续
  


                
    
    
    #最后从屏幕上移除
    window.close()   

if __name__ == "__main__":
    main()
    exit()