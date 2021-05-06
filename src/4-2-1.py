#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   minPyGame server in Python
#   Binds REP socket to tcp://*:4006
#

import time
import zmq
import messCategoryId

ctx = zmq.Context.instance()
publisher = ctx.socket(zmq.PUB)
publisher.bind("tcp://*:4005")


while True:
    #  Wait for next request from client

    #  Do some 'work'
    time.sleep(1)
    nowTime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    nowPlayerCount=1

    #  Send reply  to client
    messId=messCategoryId.MessCategory.DATEINFO.value
    publisher.send(f"{messId} 当前时间为 :{nowTime}".encode('UTF-8'))

    messId=messCategoryId.MessCategory.PLAYERINFO.value
    publisher.send(f"{messId} 当前在线人数 :{nowPlayerCount}".encode('UTF-8'))