#!/usr/bin/env python

import os

#  os.walk
#  curr_dir, dir_list, file_list

for curr_dir, dir_list, file_list in os.walk('.', topdown=True):
    if '__pycache__' in dir_list:
        dir_list.remove('__pycache__')
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print('{:10d} {}'.format(file_size, file_name))
