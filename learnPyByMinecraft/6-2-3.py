6.2.4
#  coding:utf8
#6-2-3.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import random
import time


# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

pos=mc.player.getPos()
nowX=pos.x
nowY=pos.y
nowZ=pos.z

#玩家向前走
while True:
    #玩家向前移动，即沿Z轴增加坐标
    nowZ+=0.15
    mc.player.setPos(nowX,nowY,nowZ)  
    time.sleep(2)