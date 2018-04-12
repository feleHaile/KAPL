#!/usr/bin/env python
import random

class Card():
    def __init__(self, suit, rank):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return '{}-{}'.format(
            self.rank, self.suit
        )

class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._cards = None
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                c = Card(s, r)
                self._cards.append(c)

    @property
    def cards(self):
        return [str(c) for c in self._cards]

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # dealer = property(dealer)

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string, not " + type(dealer).__name__)

    def shuffle(self):
        random.shuffle(self._cards)

    # def draw(self):
    #     return self._cards.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._cards):
            return self._cards.pop()
        else:
            raise StopIteration

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return('{}({}, {})'.format(my_name, self.dealer, len(self)))
