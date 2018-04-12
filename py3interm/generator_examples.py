#!/usr/bin/env python

hobbits = ['Frodo', 'Merry', 'Pippin', 'Bilbo', 'Sam']

eh = enumerate(hobbits)
for i, h in eh:
    print(i, h)

eh = enumerate(hobbits)
print(list(eh))
print(list(eh))
print()

with open('DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(line, end='')

a = ['Poughkeepsie', 'Newton', 'Proctor']
b = ['NY', 'MA', 'VT']

cities = zip(a, b)
print(cities)

for city, state in cities:
    print(city, state)
