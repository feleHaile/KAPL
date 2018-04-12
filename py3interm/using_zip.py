#!/usr/bin/env python

from itertools import zip_longest

a = [5, 10, 15, 18, 12]
b = [5, 10, 15, 20, 25, 30]
c = [5, 10, 17, 20, 25, 30, 35, 40]

z2 = zip_longest(a, b, c)

for row in z2:
    first = row[0]
    if all(c == first for c in row[1:]):
        print("MATCH:", row)
    else:
        print("NO MATCH:", row)
