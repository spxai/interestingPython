# /usr/bin/env python3
# -*- coding: utf-8 -*-
#2-9-4-3.py
import PySimpleGUIWeb as sg
import evalStr


def computeResult(comStr):
    return eval(comStr)
    

def main(): 

    ComputeStrLayout=[[sg.Multiline(key='computeStr',background_color='black',text_color='yellow',font="any 30",size=(60,4))]]
    numsBtLayout=[[sg.Button(i*3+j,size=(4,2),button_color=('white','green'),key=i*3+j) for j in range(1,4)] for i in range(0,3)]
    comBtLayout1= [[sg.Button('0',size=(4,2),key=0),sg.Button('.',size=(4,2),key='.')],\
        [sg.Button('(',size=(4,2),key='('),sg.Button('C',size=(4,2),key='C')],\
        [sg.Button(')',size=(4,2),key=')'),sg.Button('<=',size=(4,2),key='BackDel')],\
        ]
    comBtLayout2=[\
        [sg.Button('+',size=(4,2),key='+'),\
         sg.Button('-',size=(4,2),key='-'),\
         sg.Button('×',size=(4,2),key='*'),\
        sg.Button('÷',size=(4,2),key='/'),\
        sg.Button('=',size=(4,2),key='=')]\
    ]
    mainLayout=[[sg.Frame('',ComputeStrLayout)],\
                 [sg.Frame('',numsBtLayout),\
    sg.Column(comBtLayout1)],\
    [sg.Frame('',comBtLayout2)],\
    ]
    
    window = sg.Window('计算器', mainLayout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            #最后从屏幕上移除
            window.close()                 
            break
        if event in list(range(10)) or event in ['.','(',')','+','-','*','/']:
            window['computeStr'].update(values['computeStr']+str(event))
        elif event=='C':
            window['computeStr'].update('')
        elif event=='=':
            window['computeStr'].update("%.2f"%computeResult(values['computeStr']))
        elif event=='BackDel':
            window['computeStr'].update(values['computeStr'][:-1])

 
 

if __name__ == "__main__":
    main()
    exit()