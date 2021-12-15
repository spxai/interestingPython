#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-4-1.py
import sys, pygame
import random
import time
from pygame.locals import *
def drawCheckerBoard(screen):
    screen.blit(bjpic,(0,0)) 
    gameRectWidth=gameRectHeight=mainWidth-INTERSPACE*2
    pygame.draw.rect(screen,'blue1',(INTERSPACE,INTERSPACE,gameRectWidth,gameRectHeight),width=2)
    cellWidth=cellHeight=gameRectWidth/CELLCOUNT
    i=INTERSPACE
    while i<=gameRectHeight:
        i+=cellHeight
        pygame.draw.line(screen,'blue4',(INTERSPACE,i),(gameRectWidth+INTERSPACE,i), 1)
        pygame.draw.line(screen,'blue4',(i,INTERSPACE),(i,gameRectWidth+INTERSPACE), 1)
    pygame.display.update()
    return (cellWidth,cellHeight) 

def initCells(screen):
    cellW,cellH=drawCheckerBoard(screen)
    cellsInfo=[[[-1,(cellW*j+INTERSPACE,cellH*i+INTERSPACE)] for i in range(CELLCOUNT)] for j in range(CELLCOUNT)]
    return cellsInfo,cellW,cellH

def getPos(x,y,cellW,cellH):
    return int((x-INTERSPACE)/cellW),int((y-INTERSPACE)/cellH)

def drawCell(screen,i,j,piece,cellsMap,cellWidth,cellHeight):
 
    screen.blit(piece,cellsMap[i][j][1])
    pygame.display.flip()
    
def downPiece(screen,i,j,piece,cellsMap,cellWidth,cellHeight,nowPieceId):
        drawCell(screen,i,j,piece,cellsMap,cellWidth,cellHeight)
        cellsInfo[i][j][0]=nowPieceId




INTERSPACE=20
CELLCOUNT=40
pygame.init()
#sys.path[0]获取当前工作目录
pygame.display.set_caption("五子棋")
logo = pygame.image.load(sys.path[0]+r"\pic\3-1-4\game1.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load(sys.path[0]+r"\pic\3-1-4\bj.jpg")
bjpicRect = bjpic.get_rect()
minRect=(int(min(bjpicRect.width*0.7,bjpicRect.height*0.7)),int(min(bjpicRect.width*0.7,bjpicRect.height*0.7)))
bjpic=pygame.transform.scale(bjpic,minRect)
size = mainWidth, mainHeight =minRect
screen = pygame.display.set_mode(size)
bjpic=pygame.Surface.convert(bjpic)
piece1 = pygame.image.load(sys.path[0]+r"\pic\3-1-4\game1.png")
piece2=pygame.image.load(sys.path[0]+r"\pic\3-1-4\game2.png")
pieceRect = piece1.get_rect()

piece1=pygame.transform.scale(piece1,(mainHeight/CELLCOUNT,mainWidth/CELLCOUNT))
piece2=pygame.transform.scale(piece2,(mainHeight/CELLCOUNT,mainWidth/CELLCOUNT))
pieceRect = piece1.get_rect()



cellsInfo,cellWidth,cellHeight=initCells(screen)
nowPieceId=0
pieces=[piece1,piece2]
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
        elif event.type==pygame.MOUSEBUTTONDOWN:
            i,j=getPos(event.pos[0],event.pos[1],cellWidth,cellHeight)
            if cellsInfo[i][j][0]<0:            
                nowPieceId=(nowPieceId+1)%2
                downPiece(screen,i,j,pieces[nowPieceId],cellsInfo,cellWidth,cellHeight,nowPieceId)


    time.sleep(1)