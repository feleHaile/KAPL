#!/usr/bin/python3

import shutil
import threading
import time
from datetime import datetime

source_file = '../Data/wt.txt'
dest_file_base = 'wt'
num_copies = 50

class CopyFile(threading.Thread):

    def __init__(self,thread_name,from_file,to_file):
        threading.Thread.__init__(self,name=thread_name)
        self.from_file = from_file
        self.to_file = to_file
        self.issuccess = False
        
    def run(self):
        try:
            shutil.copyfile(self.from_file,self.to_file)
            self.issuccess = True
        except EnvironmentError as e:
            self.issuccess = False

    def success(self):
        return self.issuccess

all_threads = []

print(time.ctime())

for i in range(1,num_copies):
    t = CopyFile('thread' + str(i),source_file,"".join([dest_file_base,str(i)]))
    all_threads.append(t)
    t.start()  
    
for t in all_threads:
    t.join()
    print('*', end=' ')
    if t.success():
        print(t.name,"OK")

print(time.ctime())
