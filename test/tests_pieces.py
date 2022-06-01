import unittest
import random
from pieces import Piece, Rock_Piece, Paper_Piece, Scissors_Piece

random.seed(10)


class TestPieces(unittest.TestCase):

    def test_rock_piece(self):
        self.assertEqual(Rock_Piece, 'RO', "Rock Symbol should be 'RO'")
        self.assertEqual(Symbol.PAPER, 'PA', "Paper Symbol should be 'PA'")
        self.assertEqual(Symbol.SCISSORS, 'SC',
                         "Scissor Symbol should be 'SC'")

    def test_rock_symbol(self):
        symbol = Rock_Symbol
        self.assertEqual(symbol.wins_against(), 'SC',
                         f"{symbol.name} Symbol should win against 'SC'")
        self.assertEqual(symbol.loses_to(), 'PA',
                         f"{symbol.name} should lost against 'PA'")

    def test_paper_symbol(self):
        symbol = Paper_Symbol
        self.assertEqual(symbol.wins_against(), 'RO',
                         f"{symbol.name} Symbol should win against 'RO'")
        self.assertEqual(symbol.loses_to(), 'SC',
                         f"{symbol.name} should lost against 'SC'")

    def test_scissor_symbol(self):
        symbol = Scissors_Symbol
        self.assertEqual(symbol.wins_against(), 'PA',
                         f"{symbol.name} Symbol should win against 'PA'")
        self.assertEqual(symbol.loses_to(), 'RO',
                         f"{symbol.name} should lost against 'RO'")


if __name__ == '__main__':
    unittest.main()
