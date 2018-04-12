#!/usr/bin/python3

import inspect

class Spam:
    pass

def Ham(p1, p2='a', *p3, p4, p5='b', **p6):
    pass

for thing in (inspect, Spam, Ham):
    print("{0}: Module? {1}. Function? {2}. Class? {3}".format(
        thing.__name__,
        inspect.ismodule(thing),
        inspect.isfunction(thing),
        inspect.isclass(thing),
    ))
print()

print("Function spec for Ham:",inspect.getfullargspec(Ham))
print()

print("Current frame:",inspect.getframeinfo(inspect.currentframe()))
