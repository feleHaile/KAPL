#!/usr/bin/python3

import sys
import socket
import threading

# set up Internet TCP socket

port = 7777         # server port number

# start listening for contacts from clients
for msg in (b'spam',b'eggs', b'morespam'):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.connect(('localhost',port))
    srv.sendall(msg)
