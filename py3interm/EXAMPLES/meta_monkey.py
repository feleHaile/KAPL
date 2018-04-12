#!/usr/bin/python3

class Spam(object):
    
    def __init__(self,name):
        self._name = name
    
    def eggs(self):
        print("Good morning, {0}. Here are your delicious fried eggs.".format(self._name,))

s = Spam('Mrs. Higgenbotham')
s.eggs()

def scrambled(self):
    print("Hello, {0}. Enjoy your scrambled eggs".format(self._name,))
    
Spam.eggs = scrambled   # monkey patch the class

s.eggs()