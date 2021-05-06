#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   minPyGame server in Python
#   Binds REP socket to tcp://*:4006
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:4006")
def testConnection():
    while True:
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message.decode('UTF-8')}"  )
    
        #  Do some 'work'
        time.sleep(1)
    
        #  Send reply back to client
        socket.send(f"I received {message.decode('UTF-8')}!".encode('UTF-8'))

testConnection()