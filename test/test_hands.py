import unittest
from hands import Hand, Rock_Hand, Paper_Hand, Scissors_Hand


class TestHands(unittest.TestCase):

    def test_hand(self):
        self.assertEqual(Hand.ROCK, 'RO', "Rock Symbol should be 'RO'")
        self.assertEqual(Hand.PAPER, 'PA', "Paper Symbol should be 'PA'")
        self.assertEqual(Hand.SCISSORS, 'SC',
                         "Scissor Symbol should be 'SC'")

    def test_rock_hand(self):
        hand = Rock_Hand
        self.assertEqual(hand.wins_against(), 'SC',
                         f"{hand.name} Symbol should win against 'SC'")
        self.assertEqual(hand.loses_to(), 'PA',
                         f"{hand.name} should lost against 'PA'")

    def test_paper_hand(self):
        hand = Paper_Hand
        self.assertEqual(hand.wins_against(), 'RO',
                         f"{hand.name} Symbol should win against 'RO'")
        self.assertEqual(hand.loses_to(), 'SC',
                         f"{hand.name} should lost against 'SC'")

    def test_scissor_hand(self):
        hand = Scissors_Hand
        self.assertEqual(hand.wins_against(), 'PA',
                         f"{hand.name} Symbol should win against 'PA'")
        self.assertEqual(hand.loses_to(), 'RO',
                         f"{hand.name} should lost against 'RO'")


if __name__ == '__main__':
    unittest.main()
