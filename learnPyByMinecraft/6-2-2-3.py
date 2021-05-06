#  coding:utf8
#6-2-2-3.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import random
import time

# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

#玩家依次出现在10个随机位置
for i in range(10):
    #玩家在随机的一个位置出现
    x=random.randint(50,100)
    y=random.randint(50,100)
    z=random.randint(120,150)
    mc.player.setTilePos(x,y,z)  
    time.sleep(8)
    
