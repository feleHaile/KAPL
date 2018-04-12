#!/usr/bin/env python
from collections import defaultdict
from itertools import groupby

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

fruit_info = defaultdict(list)

for fruit in fruits:
    first_letter = fruit[0]
    fruit_info[first_letter].append(fruit)

for letter, fruits in fruit_info.items():
    print(letter, fruits)
print('*' * 60)

# fruit_info = groupby(sorted(fruits), key=lambda e: e[0])
# for letter, fruits in fruit_info:
#     print(letter, list(fruits))
