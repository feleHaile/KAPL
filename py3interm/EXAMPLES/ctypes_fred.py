#!/usr/bin/env python

import sys
from ctypes import *

class mystruct(Structure):
    _fields_ = [('x', c_int), ('y', c_int), ('name', c_char_p)]

# load the library, according to platform
if sys.platform == 'win32':
    fred = cdll.LoadLibrary('fred.dll')
elif sys.platform == 'darwin':
    fred = cdll.LoadLibrary('fred.dylib')
else:
    fred = cdll.LoadLibrary('./fred.so.1.0')

print(dir(fred))

# call a function in the library
print(fred.add(2,3))
print(fred.add(10000,9999))
try:
    print(fred.add(99999999999,99999999999999))
except Exception as e:
    print("That didn't work...", e)

# hello() calls printf() for output    
fred.hello()


# default return value type is int
# for anything else set restype
fred.get_skit.restype = c_char_p

print(fred.get_skit(1).decode())
print(fred.get_skit(4).decode())
print(fred.get_skit(99).decode())

fred.barf.restype = mystruct

m = fred.barf()
print(m)
print(dir(m))
print(m.x, m.y, m.name.decode())
