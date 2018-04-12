#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f1 = [f.upper() for f in fruits]
print(f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print(f3, '\n')

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'toast', 'spam', 'bacon', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']

x = [f for f in food if f != 'spam']
print(x, '\n')


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

last_names = [(p[1], p[2]) for p in people]
print(last_names, '\n')


