#!/usr/bin/env python

animals1 = ['cat', 'dog', 'wombat', 'sloth', 'bushbaby']

animals2 = ['sloth', 'javelina', 'coatimundi',
    'cat', 'bear', 'dog']

s1 = set(animals1)
s1.add('wallaby')

s2 = set(animals2)

print("both:", s1 & s2)
print("either:", s1 | s2)
print("just one:", s1 ^ s2)
print("just s1:", s1 - s2)
print("just s2:", s2 - s1)
