import unittest
from random import Random
from unittest.mock import patch
from rps.pieces import Rock_Piece, Paper_Piece, Scissors_Piece


class TestPieces(unittest.TestCase):

    def setUp(self):
        self.random = Random(10)

    def test_piece(self):
        pass

    @patch('rps.pieces.random')
    def test_rock_piece(self, random):
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(Rock_Piece.name, "Rock",
                         f"{Rock_Piece.name} Piece's name should be Rock.")
        self.assertEqual(Rock_Piece.symbol, "RO",
                         f"{Rock_Piece.name} Piece's symbol should be RO.")
        self.assertRaises(TypeError, Rock_Piece.move)

        rock = Rock_Piece.create((200, 200))
        self.assertEqual(rock.rect.center, (200, 200),
                         "Rock piece was not correctly created.")

        rock.move()
        self.assertEqual(rock.rect.center, (200, 205),
                         "Rock piece did not move to correct position.")

    @patch('rps.pieces.random')
    def test_paper_piece(self, random):
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(Paper_Piece.name, "Paper",
                         f"{Paper_Piece.name} Piece's name should be Paper.")
        self.assertEqual(Paper_Piece.symbol, "PA",
                         f"{Paper_Piece.name} Piece's symbol should be PA.")
        self.assertRaises(TypeError, Paper_Piece.move)

        paper = Paper_Piece.create((200, 200))
        self.assertEqual(paper.rect.center, (200, 200),
                         "Paper piece was not correctly created.")

        paper.move()
        self.assertEqual(paper.rect.center, (200, 205),
                         "Paper piece did not move to correct position.")

    @patch('rps.pieces.random')
    def test_scissor_piece(self, random):
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(Scissors_Piece.name, "Scissors",
                         f"{Scissors_Piece.name} Piece's name should be \
                         Scissors.")
        self.assertEqual(Scissors_Piece.symbol, "SC",
                         f"{Scissors_Piece.name} Piece's symbol should be SC.")
        self.assertRaises(TypeError, Scissors_Piece.move)

        scissors = Scissors_Piece.create((200, 200))
        self.assertEqual(scissors.rect.center, (200, 200),
                         "Scissors piece was not correctly created.")

        scissors.move()
        self.assertEqual(scissors.rect.center, (200, 205),
                         "Scissors piece did not move to correct position.")


if __name__ == '__main__':
    unittest.main()
