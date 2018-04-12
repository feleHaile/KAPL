
import sys
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("localhost",7777))

if len(sys.argv) > 1:
   msg = sys.argv[1]
else:
   msg = "default message"

s.send(msg)

reply = s.recv(4096)

print("Server said >",reply,"<")

s.close()
