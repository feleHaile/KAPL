#!/usr/bin/env python

import sys
import os
import stat

if len(sys.argv) < 2:
    sys.stderr.write('Please specify a starting directory\n')
    sys.exit(1)

start_dir = sys.argv[1]

for curr_dir, dir_names, file_names in os.walk(start_dir):
    for file_name in file_names:
        full_path = os.path.join(curr_dir, file_name)
        mode=stat.S_IMODE(os.lstat(full_path)[stat.ST_MODE])
        permstr = ''
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                # construct bitmasks such as stat.S_IRUSR or stat.S_IXOTH
                bitmask = getattr(stat,"S_I"+perm+level)
                if mode & bitmask:
                    permstr += perm.lower()
                else:
                    permstr += '-'
                    
        # print raw permission bits, permission string, and file name 
        print("{0:012b} {1} {2}".format(mode, permstr, file_name))
