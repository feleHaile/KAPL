#!/usr/bin/env python

"""

@author: jstrick
Created on Sun Mar 17 09:58:06 2013

"""
import sys
import re
import fileinput
import argparse

arg_parser = argparse.ArgumentParser(description="Emulate grep with python")

arg_parser.add_argument(
    '-i',
    dest='ignore_case', action='store_true',
    help='ignore case'
)

arg_parser.add_argument(
    'pattern', help='Pattern to find (required)'
)

arg_parser.add_argument(
    'filenames',nargs='*',
    help='filename(s) (if no files specified, read STDIN)'
)

args = arg_parser.parse_args()

print('-' * 40)
print(args)
print('-' * 40)

regex = re.compile(args.pattern, re.I if args.ignore_case else 0)

# print(sys.argv)

for line in fileinput.input(args.filenames):
    if regex.search(line):
        print(line, end=' ')

