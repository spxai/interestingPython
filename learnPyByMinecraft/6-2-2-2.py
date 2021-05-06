#  coding:utf8
#6-2-2-2.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import random

# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")



#玩家在随机的一个位置出现
x=random.randint(0,50)
y=random.randint(0,50)
z=random.randint(120,150)
mc.player.setTilePos(x,y,z)