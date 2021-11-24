#      /usr/bin/env python3
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

def UpdateStatus(statusStr,window):
    print(statusStr)
    #window['-OUTPUT-'].update(statusStr+ "\n"+window['-OUTPUT-'].Get())

    
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
    UpdateStatus(gameShowMess[1] + str(nRes) + "      总点数:"+ str(GetPlayerSum()),window) 
    return GetPlayerSum()
    
    
def AddComputerNum(window):
    nRes=AddRndNum(GamePlayer.COMPUTER)
    UpdateStatus(gameShowMess[3] + str(nRes) + "      总点数:"+ str(GetComputerSum()),window) 
    return GetComputerSum()
    
def GetPlayerSum():
    return playerNumSum
def GetComputerSum():
    return computerNumSum
    
def isGameOver(isGameContine):
    computerWin=playerWin=gameOver=False
    if  GetPlayerSum()>21 and GetComputerSum()<=21 :
        computerWin=True 
        playerWin=False  
        gameOver=True
    elif  GetComputerSum()>21 and GetPlayerSum()<=21:
        computerWin=False 
        playerWin=True 
        gameOver=True
    elif  GetComputerSum()>=21 and GetPlayerSum()>=21:
        gameOver=True
    elif (not isGameContine):
        if  GetComputerSum()>GetPlayerSum():
            computerWin=True
            playerWin=False 
            gameOver=True  
        elif GetComputerSum()==GetPlayerSum():
            gameOver=True  
        else:
            computerWin=False 
            playerWin=True 
            gameOver=True   
        
    return (computerWin,playerWin,gameOver)

def main():   
    global playerNums,playerNumSum,computerNums,computerNumSum,computerWin,playerWin

    # 定义窗口内容
    layout = [  [sg.Text("您是否继续抽数？")],            
                [sg.Button('Yes'), sg.Button('No'),sg.Button('Exit')],
                [sg.Output(size=(40,2), key='-OUTPUT-')]]
    
    # 创建窗口
    window = sg.Window('21点游戏', layout)      
    
    isComputerContinue=True
    isPlayerContinue=True
    #显示和与窗口交互
    while True:
        if isPlayerContinue:
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
            UpdateStatus("玩家放弃抽数",window)
            
        if isComputerContinue and GetComputerSum()<17:
            UpdateStatus("电脑确定抽数",window) 
        else:
            UpdateStatus("电脑放弃抽数",window) 
            isComputerContinue=False
            
        if isPlayerContinue:  
            AddPlayerNum(window)
        if isComputerContinue :
            AddComputerNum(window)
        if isComputerContinue or isPlayerContinue:
            (cWin,pWin,isGameEnd)=isGameOver(True)
        else:
            (cWin,pWin,isGameEnd)=isGameOver(False)
            isGameRestart=True         
        isGameRestart=False
        if pWin:
            UpdateStatus("玩家赢了",window)
            isGameRestart=True          
        elif cWin:
            UpdateStatus("电脑赢了",window)  
            isGameRestart=True 
        
        if (not pWin) and (not cWin) and isGameEnd:
            UpdateStatus("电脑和玩家都没有赢",window)
            isGameRestart=True 

                
           
        if  isGameRestart:
            UpdateStatus(" 玩家总点数:"+ str(GetPlayerSum())+"！电脑总点数："+ str(GetComputerSum()),window) 
            isComputerContinue=True
            isPlayerContinue=True
            playerNums=[]
            playerNumSum=0
            computerNums=[]
            computerNumSum=0
            computerWin=False
            playerWin=False  
            UpdateStatus("游戏重新开始",window)


  


                
    
    
    #最后从屏幕上移除

    window.close()   

if __name__ == "__main__":
    main()
    exit()