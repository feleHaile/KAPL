#!/usr/bin/env python
import unittest
import logging
import sys
from carddeck import CardDeck

logging.basicConfig(filename='TestCardDeck.log', level=logging.INFO)

class TestCardDeck(unittest.TestCase):

    def setUp(self):
        self.d = CardDeck('Test User')

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_deck_has_52_cards(self):
        self.assertEqual(52, len(self.d), "Deck does not have 52 cards")

    def test_drawing_one_card_reduces_size_of_deck(self):
        old_len = len(self.d)
        try:
            next(self.d)
        except StopIteration:
            self.assertFalse(1, 'Next card raised StopIteration')
        new_len = len(self.d)
        self.assertEqual(old_len - 1, new_len, "Drawing one card does not shorten length of deck")

    @unittest.skipUnless(sys.platform == 'win32', "Only implemented on Windows")
    def test_dealer_name_rejects_non_str(self):
        with self.assertRaises(Exception) as cm:
            sys.stdout.write(str(cm.exception) + '\n')
            d = CardDeck(1234)



if __name__ == '__main__':
    unittest.main(verbosity=2)
