#!/usr/bin/python3

class Rabbit: 

    def __init__(self,size,danger): 
        self._size = size
        self._danger = danger 
        self._victims = []

    def threaten(self):
        print("I am a {0} bunny with {1}!".format(self._size, self._danger))

r1 = Rabbit('large',"sharp, pointy teeth")
r1.threaten()

r2 = Rabbit('small','fluffy fur')
r2.threaten()

