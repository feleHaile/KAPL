#!/usr/bin/env python
# (c) 2016 John Strickler
#
from filefilter import FileFilter

@FileFilter.register
def make_upper(s):
    return str(s).upper()

@FileFilter.register
def truncate(s):
    return s[:25]

@FileFilter.register
def trim_end(s):
    return s.rstrip('\n\r')

with FileFilter('../DATA/alice.txt') as f:
    for line in f:
        print(line)

