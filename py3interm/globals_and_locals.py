#!/usr/bin/env python
from pprint import pprint

x = 5
y = 'wombat'
def spam():
    print("Python is weird and wonderful")

pprint(globals())
print(globals()['y'])

g = globals()
g['color'] = 'blue'

print(color)
print(g['spam'])
g['spam']()

def ham():
    name = 'Bob'
    print(locals())

ham()
