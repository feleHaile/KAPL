#!/usr/bin/python3
import sys
from datetime import date

color = 'blue'
animal = 'iguana'

print('{0} {1}'.format(color,animal))

fahr = 98.6839832
print('{0:.1f}'.format(fahr))

fruits = [ 'apple', 'mango', 'banana', 'cherry',
    'watermelon', 'pineapple']

print("{0[0]} {0[1]} {0[5]}".format(fruits))

airports = { 'IAD':'Dulles', 'YKF':'Waterloo International',
    'SEA':'Seattle-Tacoma' }

print("{0[IAD]}/{0[YKF]}".format(airports))

d = date(2012,1,1)

print("{0.month} {0.day} {0.year}".format(d))
print("{0.month:02d}/{0.day:02d}/{0.year:04d}".format(d))

class Movie(object):
    def __init__(self,title,director):
        self._title = title
        self._director = director
    
    @property
    def Title(self):
        return self._title
    
    @property
    def Director(self):
        return self._director

movies = [
    Movie('Jaws','Spielberg'),
    Movie('Psycho','Hitchcock')
]

for m in movies:
    print('{0.Title} by {0.Director}'.format(m))