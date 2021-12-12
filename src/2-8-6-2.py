# /usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-6-2.py
import PySimpleGUIWeb as sg
import random 

MAX_ROWS = MAX_COLS = 10
MAX_MINES_COUNT=20
MINE_TAG=-1
NO_MINE_TAG=0

def getMineMap():
    mineBits=random.sample([(i, j) for i in range(MAX_ROWS) for j in range(MAX_COLS)],k=MAX_MINES_COUNT)
    minesInfo=[[0 for i in range(MAX_ROWS)] for j in range(MAX_COLS)] 
    for x,y in mineBits:  
        minesInfo[x][y]=MINE_TAG
    for minePos in mineBits:
        x,y=minePos
        aroundPos=getAroundPos(x,y)
        for i,j in aroundPos:
            if minesInfo[i][j]>=NO_MINE_TAG :
                minesInfo[i][j]+=1
    return minesInfo

def getAroundPos(x,y):
    aroundPosAdd=[(xAdd,yAdd) for xAdd  in [-1,0,1] for yAdd in [-1,0,1]]
    aroundPos=[(x+xAdd,y+yAdd) for xAdd,yAdd in aroundPosAdd if x+xAdd>=0 and y+yAdd>=0 and x+xAdd<MAX_ROWS and y+yAdd<MAX_COLS]
    return aroundPos
    
def main():   
    minesInfo =getMineMap()
    mainLayout =  [[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COLS)] for i in range(MAX_ROWS)]
    
    window = sg.Window('扫雷', mainLayout)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # window[(row, col)].update('New text')   # To change a button's text, use this pattern
        # For this example, change the text of the button to the board's value and turn color black
        window[event].update(minesInfo[event[0]][event[1]], button_color=('Green','black'))
    
    #最后从屏幕上移除

    window.close()   

if __name__ == "__main__":
    main()
    exit()