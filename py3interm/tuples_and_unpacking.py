#!/usr/bin/env python

person = 'Bob', 'Smith', 'CA', 32

print(person[1], '\n')

# unpacking
first_name, last_name, state, age = person

people = [
    ('Melinda', 'Gates', 'Gates Foundation', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'git'),
]

for first_name, last_name, *products in people:
    print(first_name, last_name, products)
print('*' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


