
#  coding:utf8
#6-2-5.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft




# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z

#放2个石头砖块
z=z+5
mc.setBlock(x,y,z,103)
mc.setBlock(x,y+1,z,103)