
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

#放2个石头砖块
z=z+5
mc.setBlock(x,y,z,BLOCK.STONE.id)
mc.setBlock(x,y+1,z,BLOCK.STONE.id)