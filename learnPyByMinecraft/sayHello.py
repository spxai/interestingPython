
# coding:utf8

# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import datetime
import time

# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")


# 发送消息
now = datetime.datetime.now()
nowStr=now.strftime("%Y/%m/%d %H:%M:%S")





while True:
    # 获得玩家位置
    pos = mc.player.getTilePos()       
    mc.postToChat(f"今天是：{nowStr}[思普兴智能] ，您的位置是({pos.x},{pos.y},{pos.z})")
    time.sleep(5)


 
    

