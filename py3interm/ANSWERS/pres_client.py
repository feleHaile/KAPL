#!/usr/bin/python

import socket

for n in range(1,45):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect( ('localhost',7777) )
    c.send('{0} LNAME\n'.format(n).encode())
    lname = c.recv(1024).strip().decode()
    c.send( '{0} FNAME\n'.format(n).encode())
    fname = c.recv(1024).strip().decode()
    c.close()
    
    print('%s %s' % (fname,lname))
