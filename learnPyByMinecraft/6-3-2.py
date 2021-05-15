#  coding:utf8
#6-3-2.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import math



def getCirclePos(a,b,r,x):
    """根据标准方程求解圆曲线"""
    y=math.sqrt(r**2-(x-a)**2)+b
    return (x,y)
    


# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

pos=mc.player.getPos()
nowX=0
nowY=80
nowZ=pos.z+1
a=int(nowX)
b=int(nowY)
r=20
#空中画圆
for x in  range(a-r,a+r):
    nowPos=getCirclePos(a,b,r,x)
    nowX,nowY=nowPos
    mc.setBlock(nowX,nowY,nowZ,'SAND')
    mc.setBlock(nowX,-nowY,nowZ,'SAND') 

