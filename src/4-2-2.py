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
subscriber = ctx.socket(zmq.SUB)
subscriber.connect("tcp://localhost:4005")
messId=messCategoryId.MessCategory.DATEINFO.value
subscriber.setsockopt(zmq.SUBSCRIBE,messId.encode('UTF-8'))



while True:

    #  Do some 'work'
    time.sleep(1)
    message = subscriber.recv()

    print(message.decode('UTF-8'))
