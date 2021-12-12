# /usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-6-1.py
import PySimpleGUIWeb as sg
from random import randint
MAX_ROWS = MAX_COL = 10

def main():   
    mineAroundCount = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
    
    mainLayout =  [[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
    
    window = sg.Window('扫雷', mainLayout)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # window[(row, col)].update('New text')   # To change a button's text, use this pattern
        # For this example, change the text of the button to the board's value and turn color black
        window[event].update(board[event[0]][event[1]], button_color=('Green','black'))
    
    #最后从屏幕上移除

    window.close()   

if __name__ == "__main__":
    main()
    exit()