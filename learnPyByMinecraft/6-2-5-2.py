#  coding:utf8
#6-2-5-2.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import time
import math



def getCirclePos(a,b,r,x):
    """根据标准方程求解圆曲线"""
    y=math.sqrt(r**2-(x-a)**2)+b
    return (x,y)
    


# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

pos=mc.player.getPos()
nowX=pos.x
nowY=40
nowZ=pos.z
a=0
b=0
r=30
#玩家空中盘旋飞行
while True:
    for x in  range(a-r,a+r):
        nowPos=getCirclePos(a,b,r,x)
        nowX,nowZ=nowPos
        mc.player.setPos(nowX,nowY,nowZ)  
        time.sleep(0.1)
    for x in  range(a+r,a-r,-1):
        nowPos=getCirclePos(a,b,r,x)
        nowX,nowZ=nowPos
        nowZ=-nowZ
        mc.player.setPos(nowX,nowY,nowZ)  
        time.sleep(0.1)