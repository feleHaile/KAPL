#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
print(mary_in)

print(mary_in.closed)
print()

with open('DATA/mary.txt') as mary_in:
    whole_file = mary_in.read()
print(whole_file)
print(repr(whole_file))

s = 'foo'
print(s)
print(str(s))
print(repr(s))

x = [1, 2, 3]
print(x)

print(None)
print(True)


fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitlist.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

