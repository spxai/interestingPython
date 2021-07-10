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

def updateStatus(statusStr,window):
    window['-OUTPUT-'].update(window['-OUTPUT-'].Get()+ statusStr)
    
def AddRndNum(gamePlayer):
    if gamePlayer==GamePlayer.COMPUTER:
        computerNum=rnd.randint(1,10)
        computerNums.append(computerNum)  
        computerNumSum+=computerNum
        return computerNumSum        
    else:            
        playNum=rnd.randint(1,10)
        playerNums.append(playNum)
        playerNumSum+=playNum
        return playerNumSum

def UpdateIsGameOver(gamePlayer,numSum):
    if gamePlayer==GamePlayer.COMPUTER and numSum>21:
        computerWin=False
        playerWin=True           
    if gamePlayer==GamePlayer.PLAYER and numSum>21:
        computerWin=True
        playerWin=False    
    return (computerWin,playerWin)

def main():   
    gameShowMess=["玩家停止抽数！","玩家继续抽数：","电脑停止抽数","电脑抽数："]
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
                updateStatus("玩家确定抽数")
            elif event == 'No':
                updateStatus("玩家放弃抽数")  
                isPlayerContinue=False      
        else:
            updateStatus("玩家放弃抽数")   
        if isComputerContinue :
            updateStatus("电脑确定抽数") 
        else:
            updateStatus("电脑放弃抽数")            
            
        if isPlayerContinue:  
            (cWin,pWin)=UpdateIsGameOver(GamePlayer.PLAYER,AddPlayerNum())  
        if isComputerContinue :
            (cWin,pWin)=UpdateIsGameOver(GamePlayer.COMPUTER,AddComputerNum())
        if cWin or pWin:
            #有一方赢了，游戏结束
        else:
            #游戏没有结束，继续
  

    
            
        int(values[0])
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

if __name__ == "__main__":
    main()
    exit()