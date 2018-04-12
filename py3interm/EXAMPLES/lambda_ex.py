#!/usr/bin/python3

fruits = ['watermelon','Apple','Mango','KIWI','apricot','LEMON','guava']

sfruits = sorted(fruits,key=lambda e: e.lower())

print(" ".join(sfruits))

