#!/usr/bin/env python
from shutil import rmtree
import os

# for x in dir(os):
#     if not x.startswith('_') and x[0].islower():
#         print(x)

print(os.access('/etc/passwd', os.R_OK))
print(os.access('/etc/passwd', os.W_OK))
print(os.access('/etc/passwd', os.X_OK))

print(os.getcwd())
print(os.getuid())

print(os.listdir('DATA'))
print('=' * 60)
for entry in os.scandir('DATA'):
    print(entry.name)

os.remove('doomed_file.txt')
rmtree('foobar')  # remove entire file tree (like rm -rf)
