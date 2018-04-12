#!/usr/bin/env python
import types
import inspect
import typing

from ANSWERS.president import President

p = President(27)

print(p.first_name, p.last_name, '\n')

fields = 'first_name', 'term_start_date', 'party'

for f in fields:
    print(f, getattr(p, f))
print()

print(hasattr(p, 'birth_place'))

setattr(President, 'assassinated', False)

print(p.assassinated)

setattr(p, 'color', 'blue')

print(p.color)

delattr(p, 'color')

# print(p.color)

def bark(self):
    print("woof woof")

setattr(President, 'bark', bark)

p.bark()

def get_out_of_bathtub(self):
    print("OOWWWWWOOOWWW")

setattr(p, "get_out_of_bathtub", types.MethodType(get_out_of_bathtub, p))

p.get_out_of_bathtub()

def bilal():
    print("I AM STATIC")

setattr(President, 'bilal', staticmethod(bilal))

p.bilal()
print()

attrs = [a for a in dir(p) if not a.startswith('_')]
print(attrs, '\n')

for a in attrs:
    print(f'{a:20} {getattr(p, a)}')

print(inspect.isclass(President))
print(inspect.isclass(p))
print(inspect.ismethod(p.bark))

def all_params(pn: typing.Iterable, p1:str, p2:int=1234, *p3, p4:str, p5:int='wombat', **p6) -> typing.List:
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print("p6:", p6)
    print('=' * 10)

print(inspect.getfullargspec(all_params), '\n')
