# coding:utf8
#4-1-2.py

# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import datetime
import time

# 建立mc连接对象
mc = minecraft.Minecraft.create()


# 发送消息
#获取当前时间
now = datetime.datetime.now()
nowStr=now.strftime("%Y/%m/%d %H:%M:%S")





while True:
    # 获得玩家位置
    pos = mc.player.getTilePos()       
    #向玩家输出当前时间和位置
    mc.postToChat(f"现在时间是：{nowStr} ，您的位置是({pos.x},{pos.y},{pos.z})")
    time.sleep(5)