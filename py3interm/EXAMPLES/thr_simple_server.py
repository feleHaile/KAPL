#!/usr/bin/python3

"""
 thr_simple_server.py
 
 simple illustration of threading module
 multiple clients connect to server; each client repeatedly sends a
 value k, which the server adds to a global string v and echoes back
 to the client; k = '' means the client is dropping out; when all
 clients are gone, server prints final value of v
"""
import socket
import threading

# class for threads, subclassed from threading.Thread class
class srvr(threading.Thread):
    # v and vlock are class variables
    v = b''
    vlock = threading.Lock()

    # I want to give an ID number to each thread, starting at 0
    def __init__(self,clntsock):
        # invoke constructor of parent class
        super().__init__()
        # add instance variables
        self._myclntsock = clntsock

    def run(self):
        """
        this function is what the thread actually runs; 
        the required name is run(); 
        threading.Thread.start() calls threading.Thread.run(),
        which is always overridden, as we are doing here
        """
        while 1:
            # receive letter from client, if it is still connected
            k = self._myclntsock.recv(256)
            if len(k) == 0:
                break
            # update v in an atomic manner
            #srvr.vlock.acquire()
            print("k is >{}<".format(k))
            srvr.v += k
            #srvr.vlock.release()
            self._myclntsock.close()

# set up Internet TCP socket
lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 7777         # server port number
# bind lstn socket to this port
lstn.bind(('', port))

# start listening for contacts from clients (at most 2 at a time)
lstn.listen(5)

nclnt = 3         # number of clients

mythreads = [] # list of all the threads
# accept calls from the clients

for i in range(nclnt):
	# wait for call, then get a new socket to use for this client,
	# and get the clients address/port tuple (though not used)
	(clnt,ap) = lstn.accept()
	
	# make a new instance of the class srvr
	s = srvr(clnt)
	
	# keep a list of all threads
	mythreads.append(s)
	
	# threading.Thread.start calls threading.Thread.run(), which we
	# overrode in our definition of the class srvr
	s.start()
	
# shut down the server socket, since it's not needed anymore
# lstn.close()
	
# wait for all threads to finish
for s in mythreads:
    s.join()
print('the final value of v is', srvr.v)