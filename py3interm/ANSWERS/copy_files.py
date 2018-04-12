#!/usr/bin/env python
import sys
import os
import shutil

DEST = '../TEMP'

for dir_path, dir_list, file_list in os.walk('..'):
    if 'TEMP' not in dir_path:
        for file_name in file_list:
            if file_name.endswith('.txt'):
                full_name = os.path.join(dir_path, file_name)
                print(full_name)
                shutil.copy(full_name, DEST)
