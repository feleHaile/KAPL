#!/usr/bin/python3

class Special(object):
    
    def __init__(self,value):
        self._value = str(value)  # all Special objects are strings
    
    # define what happens when a Special object is added to another Special object
    def __add__(self,other):
        return self._value + other._value
    
    # define what happens when a Special object is multiplied by a value
    def __mul__(self,num):
        return ''.join((self._value for i in range(num)))
    
    # define what happens when str() called on a Special object
    def __str__(self):
        return self._value.upper()

    # define equality between two Special valuess
    def __eq__(self,other):
        return self._value == other._value
    
if __name__ == '__main__':
    s = Special('spam')
    t = Special('eggs')
    u = Special('spam')
    v = Special(5)
    w = Special(22)
    
    print("s + s", s + s)
    print("s + t", s + t)
    print("t + t", t + t)
    print("s * 10", s * 10)
    print("t * 3", t * 3)
    print("str(s)={0}  str(t)={1}".format( str(s), str(t) ))
    print("id(s)={0} id(t)={1} id(u)={2}".format( id(s), id(t), id(u) )) 
    print("s == s", s == s)
    print("s == t", s == t)
    print("u == s", s == u)
    print("v + v", v + v)
    print("v + w", v + w)
    print("w + w", w + w)
    print("v * 10", v * 10)
    print("w * 3", w * 3)
