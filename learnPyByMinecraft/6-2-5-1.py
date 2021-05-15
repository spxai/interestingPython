#  coding:utf8
#6-2-5-1.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import time
import math



def getCirclePos(a,b,r,circleTheta):
    """根据参数方程求解圆曲线"""
    x = a + r * math.cos(circleTheta)
    y = b + r * math.sin(circleTheta)
    return (x,y)
    


# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

pos=mc.player.getPos()
nowX=pos.x
nowY=40
nowZ=pos.z
 

#玩家空中盘旋飞行
while True:
    for ctht in  range(int(2*math.pi*100),0,-5):
        nowPos=getCirclePos(0,0,30,ctht/100)
        nowX,nowZ=nowPos
        mc.player.setPos(nowX,nowY,nowZ)  
        time.sleep(0.1)
