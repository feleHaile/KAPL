#!/usr/bin/python3

import shutil
import threading
import time
from datetime import datetime

source_file = '../DATA/wt.txt'
dest_file_base = 'wt'
num_copies = 375

print(time.ctime())

# non-threaded version
for i in range(1,num_copies):
    shutil.copyfile(source_file,"".join((dest_file_base,"_",str(i))))

print(time.ctime())
