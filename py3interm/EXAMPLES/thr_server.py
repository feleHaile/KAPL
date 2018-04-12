import socket
import threading

class HandleClient(threading.Thread):

    def __init__(self,sock,num):
        threading.Thread.__init__(self)
        self.sock = sock
        self.num = num

    def run(self):
        print("Thread",self.num,"at your service")
        request = b''
        while True:
            chunk = self.sock.recv(1024)
            if len(chunk) == 0:
               break
            request += chunk
 
        print("Client said: >{0}<".format(request.decode().rstrip()))
        request_str = ''.join(chr(c) for c in request)
        reply = (request_str.upper() + " ") * 3
        self.sock.send(reply.encode())
        self.sock.close()

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.bind((socket.gethostname(),7777))

serv.listen(5)

tnum = 0
while True:
    (csock,addr) = serv.accept()
    t = HandleClient(csock,tnum)
    t.start()
    tnum += 1
    
