#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Spam():
    pass

class Pet(Spam):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class Animal(Spam, metaclass=ABCMeta):

    @abstractmethod
    def make_noise(self):
        print("MAKING NOISE:")

class Dog(Pet, Animal):
    def __init__(self, name):
        Animal.__init__(self)
        Pet.__init__(self, name)

    def make_noise(self):
        super().make_noise()
        print("Woof! Woof!")

d = Dog('Fido')
d.make_noise()
print(d.name)
print(Dog.mro())
