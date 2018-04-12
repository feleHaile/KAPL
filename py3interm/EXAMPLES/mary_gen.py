#!/usr/bin/python3

def chomper(file_obj):
    for line in file_obj:
        if line.endswith('\n'):
            line = line[:-1]
        yield line

m = open('../DATA/mary.txt')
for line in chomper(m):
    print(line)
m.close()

