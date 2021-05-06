
#  coding:utf8
#6-2-4.py
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

#玩家随机走
while True:
    #玩家移动，即沿Z、X轴增加或减少随机数(0~0.5)
    rndNum=random.randint(-10,10)
    if abs(rndNum) % 2 ==0:
        nowZ+=rndNum/20
        nowX+=rndNum/20
    else:
        nowZ+=rndNum/20
        nowX+=rndNum/20
    mc.player.setPos(nowX,nowY,nowZ)  
    time.sleep(2)