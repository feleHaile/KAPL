#!/usr/bin/python3
import queue
import random
from threading import Thread,Lock as tlock
import time

NUM_ITEMS = 25000
POOL_SIZE = 100

q = queue.Queue(0)

shared_list = []
shlist_lock = tlock()
stdout_lock = tlock()

import random

class Words(object):
    def __init__(self):
        with open('../DATA/words.txt') as WORDS:
            self._words = [word[:-1] for word in WORDS.readlines()]
        self._num_words = len(self._words)
        
    def GetRandomWord(self):
        return self._words[random.randrange(0,self._num_words)]

class Worker(Thread):
    
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        while True:
            try:
                s1 = q.get(block=False)
                s2 = s1.upper() + '-' + s1.upper()
                shlist_lock.acquire()
                shared_list.append(s2)
                shlist_lock.release()
                stdout_lock.acquire()
                stdout_lock.release()

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

print(shared_list[:20])

print(start_time)
print(end_time)
