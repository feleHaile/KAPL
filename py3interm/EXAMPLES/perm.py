#!/usr/bin/python3
import sys
import os
import stat
import glob

if len(sys.argv) < 2:
    sys.stderr.write('Please specify a starting directory\n')
    sys.exit(1)

start_dir = sys.argv[1]

if len(sys.argv) == 3:
    file_pattern = sys.argv[2]
else:
    file_pattern = "*"

for dirname,dirlist,filelist in os.walk(start_dir):
    path = os.path.join(dirname,file_pattern)
    for file_name in glob.iglob(path):
        mode=stat.S_IMODE(os.lstat(file_name)[stat.ST_MODE])
        permstr = ''
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                if mode & getattr(stat,"S_I"+perm+level):
                    permstr += perm
                else:
                    permstr += '-'
        print(permstr,file_name)
