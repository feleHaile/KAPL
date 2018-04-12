#!/usr/bin/env python

while True:
    file_name = input("File name: ")
    if file_name == 'q':
        break
    if file_name == '':
        continue
    print("deleting", file_name)
