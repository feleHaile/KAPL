#!/usr/bin/python3
import queue
import random
from threading import Thread,Lock as tlock
import time
import sys

NUM_ITEMS = 10000
POOL_SIZE = 3

q = queue.Queue(0)

file_lock = tlock()

import random

class Words(object):
    def __init__(self):
        with open('../DATA/words.txt') as WORDS:
            self._words = [word[:-1] for word in WORDS.readlines()]
        self._num_words = len(self._words)
        
    def GetRandomWord(self):
        return self._words[random.randrange(0,self._num_words)]

class Worker(Thread):
    Thread._outfile = open('queue_output.txt','w') 
    
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        while True:
            try:
                s1 = q.get(block=False)
                s2 = s1.upper() + '-' + s1.upper()
                file_lock.acquire()
                Thread._outfile.write(s2 + "\n")
                file_lock.release()

            except queue.Empty:
                break

# fill the queue
words = Words()
for i in range(NUM_ITEMS):
    w = words.GetRandomWord()
    q.put(w)

start_time = time.ctime()

# populate the threadpool
pool = []
for i in range(POOL_SIZE):
    name = "Worker {0:c}".format(i+65)
    w = Worker(name)  # add thread to pool
    w.start()
    pool.append(w)
    
for t in pool:
    t.join() 

end_time = time.ctime()

print(start_time)
print(end_time)
