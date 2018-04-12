#!/usr/bin/python3

class Knight(object):
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

k = Knight("Lancelot")
k.color = 'blue'

# Bridgekeeper's question
print('Sir {0}, what is your...favorite color?'.format( k.name ))
# Knight's answer
print("red, no -- {0}!".format( k.color ))
