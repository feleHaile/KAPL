#!/usr/bin/env python
"""
Exercise the CardDeck class.
"""
from carddeck import CardDeck

CD1 = CardDeck('Manny')
print(CD1)

CD2 = CardDeck('Mo')

print(CD1.dealer)

CD1.dealer = 'Abe'

print(CD1.dealer)

try:
    CD1.dealer = 123
except TypeError as err:
    print(err)

try:
    CD3 = CardDeck(None)
except TypeError as err:
    print(err)

print(CD1.cards)
print()
CD1.shuffle()
print(CD1.cards)

HAND = []
for i in range(5):
    HAND.append(next(CD1))
print("hand:", [str(c) for c in HAND])

for card in CD2:
    print(card)
print()

print(len(CD1), len(CD2))
print(CD1)
