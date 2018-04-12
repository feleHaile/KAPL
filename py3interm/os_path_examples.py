#!/usr/bin/env python
from datetime import datetime
import os  # os.path auto-imported
from humanfriendly import format_size

FOLDER = 'DATA'
FILE = 'alice.txt'

file_path = os.path.join(FOLDER, FILE)
print("path:", file_path)

file_size = os.path.getsize(file_path)
print("size:", format_size(file_size))

raw_timestamp = os.path.getmtime(file_path)
print("raw ts:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)

print('stat info:', os.stat(file_path))

print('absolute path:', os.path.abspath(file_path))
print('basename:', os.path.basename(file_path))
print('dirname:', os.path.dirname(file_path))


print(format_size(234723984723, binary=False))
