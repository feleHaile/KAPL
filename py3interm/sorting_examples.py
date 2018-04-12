#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print(f1, '\n')

f2 = sorted(fruits, key=str.lower)
print(f2, '\n')

f3 = sorted(fruits, key=len)
print(f3, '\n')

def fruit_compare(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=fruit_compare)
print(f4, '\n')

def by_last_name(person):
    return person[1], person[0]

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]


p1 = sorted(people, key=by_last_name)
for first_name, last_name, _ in p1:
    print(first_name, last_name)
print('*' * 60)

p2 = sorted(people, key=lambda e: (e[1], e[0]))
for first_name, last_name, _ in p1:
    print(first_name, last_name)
print('*' * 60)

f5 = sorted(fruits, key=lambda e: (len(e), e.lower()))
print(f5, '\n')
