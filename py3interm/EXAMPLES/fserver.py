#!/usr/bin/python3

import socket
import sys
import os
import threading

def handle_client(client,num):
        pid = os.fork()
        if pid:   # in parent
            return  # nothing to do if in parent
        request = client.recv(1024)
        reply = (request.upper() + " ") * 3
        client.send(reply)
        client.close()
        sys.exit(1)  # exit from child process
       
serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.bind((socket.gethostname(),7777))

serv.listen(5)

server_count = 0
while True:
    (csock,addr) = serv.accept()
    handle_client(csock,server_count)

    server_count += 1

