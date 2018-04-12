#!/usr/bin/env python

def open_nonl(file_path):
    with open(file_path) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')
    # raise StopIteration

mary_in = open_nonl('DATA/mary.txt')
for line in mary_in:
    print(line)
print('-' * 60)

def giant():
    yield "fee"
    yield "fi"
    yield "fo"
    yield "fum"


g = giant()
for word in g:
    print(word)

def parse_delim_file(file_path, delimiter='\t'):
    with open(file_path) as file_in:
        for line in file_in:
            fields = line.rstrip().split(delimiter)
            yield fields

k = parse_delim_file('DATA/knights.txt', ':')
for row in k:
    print(row)`x
