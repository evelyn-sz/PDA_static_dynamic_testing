import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.club = Card("club", 1)
        self.diamond = Card("diamond", 2)
        self.heart = Card("heart", 3)
        self.spade = Card("spade", 4)
        self.card_game = CardGame()
        self.cards = [self.club, self.diamond, self.heart, self.spade]

    def test_card_has_ace_equal_1(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.club))

    def test_highest_card(self):
        self.assertEqual(self.diamond, self.card_game.highest_card(self.diamond, self.club))

    def test_cards_total(self):
        self.assertEqual("You have a total of 10", self.card_game.cards_total(self.cards))