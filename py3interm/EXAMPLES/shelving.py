#!/usr/bin/env python

import shelve

d = shelve.open("sampledata")

d['names'] = ['John','Eric','Graham','Michael', 'Terry','Terry']
d['number'] = 42
d['range'] = list(range(1,11))

d.close()

# --- usually in a different script:

d2 = shelve.open("sampledata")

for name in d2['names']:
    print(name)

d2.close()