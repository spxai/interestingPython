# /usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-6-3.py
import PySimpleGUIWeb as sg
import random 

MAX_ROWS = MAX_COLS = 10
MAX_MINES_COUNT=20
MINE_TAG='@'
NO_MINE_TAG=0
successTags=set()


mineBits=random.sample([(i, j) for i in range(MAX_ROWS) for j in range(MAX_COLS)],k=MAX_MINES_COUNT)

def getMineMap():
    minesInfo=[[0 for i in range(MAX_ROWS)] for j in range(MAX_COLS)] 
    for x,y in mineBits:  
        minesInfo[x][y]=MINE_TAG
        
    for minePos in mineBits:
        x,y=minePos
        aroundPos=getAroundPos(x,y)
        for i,j in aroundPos:
            if (i,j) not in mineBits:
                minesInfo[i][j]+=1
    return minesInfo

def getAroundPos(x,y):
    aroundPosAdd=[(xAdd,yAdd) for xAdd  in [-1,0,1] for yAdd in [-1,0,1]]
    aroundPos=[(x+xAdd,y+yAdd) for xAdd,yAdd in aroundPosAdd if x+xAdd>=0 and y+yAdd>=0 and x+xAdd<MAX_ROWS and y+yAdd<MAX_COLS]
    return aroundPos

def showAllMines(win):
    for minePos in mineBits:
        if win[minePos].get_text()=='*':
            win[minePos].update(button_color=('green','red')) 
        elif win[minePos].get_text()!=MINE_TAG:
            win[minePos].update(MINE_TAG) 
    win['gameResult'].update("本局成绩："+str(int(len(successTags)/len(mineBits)*100)))

            





    

        
def main(): 
    isGameRestart=True

    SelBtLayout = [
                    [sg.Button('不是雷',key='noTagMine')], \
                    [sg.Button('标注雷',key='tagMine')],\
                    [sg.Button('点按此格',key='clickCell')],\
                    [sg.Button('结束本局',key='showAll')],\
                    [sg.Text('本局成绩:',key='gameResult')],
                  ]
    MinesLayout =[[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0),button_color=('white','green')) for j in range(MAX_COLS)] for i in range(MAX_ROWS)]
    mainLayout=[[sg.Frame('雷区', MinesLayout, font='Any 20', title_color='green'),\
                sg.Column(SelBtLayout)],\
               [sg.Button('重新开始游戏',key='restartGame'),\
               sg.Button('退出游戏',key='exitGame')]
            ]
    window = sg.Window('扫雷', mainLayout)
    while isGameRestart:
        minesInfo =getMineMap()
        selX=selY=-1
        oldX=oldY=-1
        isGameContinue=True
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit') or event=='exitGame':
                isGameRestart=False
                #最后从屏幕上移除
                window.close()                 
                break
            elif event=='restartGame':
                showAllMines(window)  
                for i in range(MAX_ROWS):
                    for j in range(MAX_ROWS):
                        window[(i,j)].update("?",button_color=('white','green'))
                successTags.clear()                  
                break
            if isGameContinue:
                
                if event=='tagMine' and selX>=0 and selY>=0 and minesInfo[selX][selY]==MINE_TAG :
                    successTags.add((selX,selY))
                elif event=='noTagMine' and selX>=0 and selY>=0 and minesInfo[selX][selY]==MINE_TAG :
                    successTags.discard((selX,selY))  
                if event=='tagMine' or event=='noTagMine':
                    if selX>=0 and selY>=0:
    
                        if event=='tagMine':
                            if window[(selX,selY)].get_text()=='?':
                                window[(selX,selY)].update('*')
                        else:
                            if window[(selX,selY)].get_text()=='*':
                                window[(selX,selY)].update('?',button_color=('white','green'))
                elif event=='clickCell':
                    window[(selX,selY)].update(minesInfo[selX][selY],button_color=('yellow','blue'))
                    if window[(selX,selY)].get_text()==MINE_TAG:
                        window[(selX,selY)].update(minesInfo[selX][selY],button_color=('red','black'))
    
                elif event=='showAll':
                    showAllMines(window)
                    isGameContinue=False
                    
                else:
                    if oldX>=0 and oldY>=0 and window[(selX,selY)].get_text()!=MINE_TAG:
                        window[(oldX,oldY)].update(button_color=('white','green'))
                    selX=event[0]
                    selY=event[1]
                    if window[(selX,selY)].get_text()!=MINE_TAG:
                        window[event].update(button_color=('Green','black'))            
                    oldX=selX
                    oldY=selY            
            

            
            
  

if __name__ == "__main__":
    main()
    exit()