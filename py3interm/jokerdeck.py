#!/usr/bin/env python

from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _create_deck(self):
        super()._create_deck()
        self._cards.append(Card(None, "Joker1"))
        self._cards.append(Card(None, "Joker2"))

if __name__ == '__main__':
    j = JokerDeck('Ophelia')
    print(j.cards)
