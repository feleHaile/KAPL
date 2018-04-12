#!/usr/bin/env python
import argparse
import re
import fileinput
import sys

parser = argparse.ArgumentParser(
    description="A fake grep"
)

parser.add_argument('-i', dest="ignore_case", help="make search case insensitive", action="store_true")
parser.add_argument('-f', dest="print_file_name",
                    help="display file name",
                    action="store_true")

parser.add_argument('pattern', help="Pattern to find")

parser.add_argument('files', nargs='*', help="Files to search")

args = parser.parse_args()

# print(args)

re_flags = 0
if args.ignore_case:
    re_flags |= re.I

pattern = re.compile(args.pattern, re_flags)

for line in fileinput.input(args.files):
    if pattern.search(line):
        if args.print_file_name:
            print(fileinput.filename(), end=' ')
        print(line.rstrip())
