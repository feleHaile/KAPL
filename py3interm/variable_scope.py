#!/usr/bin/env python
import sys
x = 42

def print(*args, **kwargs):
    __builtins__.print('*' * 10)
    __builtins__.print(*(str(a).upper() for a in args))
    __builtins__.print('*' * 10)


#    sys.stdout.write("SUCKER!\n")

print("Hello")

def ham():
    x = 'bushbaby'

    def spam():
        y = 100
        print(x)

    return spam

s = ham()
print(s)

s()
# print(x)
