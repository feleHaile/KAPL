#!/usr/bin/env python

list1 = list()
list2 = ['spam', 'ham', 'eggs']
list3 = []
list4 = 'a b c'.split()

word = 'wombat'
list5 = list(word)
print(list5)

word = 'mississippi'
print(set(list(word)))
print()

for c in word:
    print(c)
print()

list2 = ['spam', 'ham', 'eggs']
for food in list2:
    print(food.upper())
print()

list2.append('toast')

more_food = ['beans', 'tomato', 'sausage']
list2.extend(more_food)
print(list2)

list2.insert(3, 'bacon')
print(list2)

del list2[5]
print(list2)

x = list2.pop(3)
print("x is", x)
print(list2)

list2.remove('tomato')
print(list2)
# list2.remove('jelly bean')  ERROR!!

print(list2)

list2[2:4] = ['grapefruit', 'biscuit', 'butter']
print(list2)


