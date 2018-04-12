#!/usr/bin/python3

import threading
import random
import time

class SimpleThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self._threadnum =num
    
    def run(self):
        time.sleep(random.randint(1, 3))
        print("Hello from thread {0}".format(self._threadnum))

for i in range(10):
    t = SimpleThread(i)
    t.start()

print("Done.")
