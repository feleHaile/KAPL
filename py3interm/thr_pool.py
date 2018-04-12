#!/usr/bin/env python
from multiprocessing.dummy import Pool
from datetime import date

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]


def task(word):
    return (word.upper(), len(word))

p = Pool(4)

results = p.map(task, fruits)

print(results)

def mkdate(d):
    year, month, day = d.split('-')
    return date(int(year), int(month), int(day))

values = ['2014-08-01', '1924-03-12', '1925-03-30',
          '1952-09-27', '1956-10-31', '1943-08-23',
          '1948-05-23', '1962-12-21']


p = Pool(2)
results = p.map(mkdate, values)
print(results)
