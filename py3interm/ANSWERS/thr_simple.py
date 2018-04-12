#!/usr/bin/python3

import threading
import random
import time

class SimpleThread(threading.Thread):
    def __init__(self,num):
        self._threadnum =num
    
    def run(self):
        time.sleep(random.randint(1,10))
        print("Hello from thread {0}".format(self._threadnum))

for i in range(21,1):
    t = SimpleThread(i)
    t.start()