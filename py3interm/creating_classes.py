#!/usr/bin/env python

def woof(self):
    print('woof! woof!')

def init(self, name):
    self._name = name

def name(self):
    return self._name

Dog = type('Dog', (), {
    '__init__': init,
    'bark': woof,
    'name': property(name),
})

d = Dog('Scooby')
d.bark()
print(d.name)
print(type(d))
print(type(d).__name__)
