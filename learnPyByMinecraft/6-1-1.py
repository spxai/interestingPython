
# coding:utf8
#6-1-1.py
# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft


# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")


# 发送消息
mc.postToChat("你好，世界！ hello,world!")



 
    

