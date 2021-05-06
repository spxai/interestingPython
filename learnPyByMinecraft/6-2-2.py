# coding:utf8
#6-2-2.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft

# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

# 玩家定位于(20,160,16)

x=20
y=150
z=16
mc.player.setTilePos(x,y,z)