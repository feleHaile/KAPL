#!/usr/bin/env python

import sys
import subprocess as P
from glob import glob

if sys.platform == 'win32':
    CMD_STRING = r'dir ..\DATA\t*'
    CMD_LIST = ['cmd', '/c', 'dir', '/a'] + glob(r'..\DATA\t*')
    CMD_LIST2 = ['cmd', '/c', 'dir', r'..\DATA\wildebeest.txt']
else:
    CMD_STRING = 'ls -ld ../DATA/t*'
    CMD_LIST = ['ls', '-ld'] + glob('../DATA/t*')
    CMD_LIST2 = ['ls', '-l', '../DATA/wildebeest.txt']

# call with wildcards (easiest)
print("Scenario 1:")
status = P.call(CMD_STRING, shell=True)
print("STATUS:", status)
print('-' * 50)

# call with wildcards (safest if commands do not come from trusted source)
print("Scenario 2:")
status = P.call(CMD_LIST)
print("STATUS:", status)
print('-' * 50)


# capture stdout
print("Scenario 3:")
output = P.check_output(CMD_STRING, shell=True)
print("CAPTURED STDOUT:\n", output)
print('-' * 50)

# capture stdout *and* stderr
print("Scenario 4:")
output = P.check_output(CMD_STRING, shell=True, stderr=P.STDOUT)
print("CAPTURED STDOUT:\n", output)
print('-' * 50)

# if status is not 0
print("Scenario 5:")
try:
    output = P.check_output(CMD_LIST2, stderr=None)
    print("CAPTURED STDOUT:\n", output)
except P.CalledProcessError as e:
    print("Process failed with return code", e.returncode)

print('-' * 50)

