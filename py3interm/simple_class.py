#!/usr/bin/env python

class Ham():
    def hello(self):
        print("Hello")

class Spam(Ham):
    def __str__(self):
        return "I am a happy Spam"

s = Spam()
print(s)
s.hello()
print(dir(object))
