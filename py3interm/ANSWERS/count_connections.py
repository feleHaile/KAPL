#!/usr/bin/env python

import subprocess

output = subprocess.check_output("netstat -an", shell=True)
count = 0
for line in output.decode().split('\n'):
    if 'ESTABLISHED' in line:
        count += 1

print("There are {0} established connections".format(count))
