# coding:utf8
#6-1-3.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft

# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")

# 创建1个柱子

mc.setBlock(pos.x + 1, pos.y + 1, pos.z, "minecraft:mossy_cobblestone") 
for i in range(2,30):
    mc.setBlock(pos.x + 1, pos.y+i , pos.z, "minecraft:magma_block")  