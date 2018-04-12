#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

fgen = (f.upper() for f in fruits)

print(fgen)
fruits.append('marionberry')

for fruit in fgen:
    print(fruit)
print('-' * 60)

def print_fruit_from_iter(fruit_iter):
    for fruit in fruit_iter:
        print(fruit)


print_fruit_from_iter(f.title() for f in fruits)
print('-' * 60)

print_fruit_from_iter(f.title()[:3] for f in fruits if f.startswith('p'))
print('-' * 60)
