import unittest
import pygame
from hands import Hand, Rock, Paper, Scissors
from pieces import Paper_Piece, Rock_Piece, Scissors_Piece


class TestHands(unittest.TestCase):

    def test_hand(self):
        hand = Hand()
        self.assertIsInstance(hand.group, pygame.sprite.Group,
                              "Hand group should be a sprite group.")

    def test_rock(self):
        self.assertIsInstance(Rock.piece(), Rock_Piece,
                              "Rock piece is not Rock Piece")

        rock_piece = Rock.create()
        self.assertIsInstance(rock_piece, Rock_Piece,
                              "Rock create did not create Rock Piece")

        rock = Rock()
        self.assertRaises(NotImplementedError, rock.collide)

    def test_paper(self):
        self.assertIsInstance(Paper.piece(), Paper_Piece,
                              "Paper piece is not Paper Piece")

        paper_piece = Paper.create()
        self.assertIsInstance(paper_piece, Paper_Piece,
                              "Paper create did not create Paper Piece")

        paper = Paper()
        self.assertRaises(NotImplementedError, paper.collide)

    def test_scissors(self):
        self.assertIsInstance(Scissors.piece(), Scissors_Piece,
                              "Scissors piece is not Scissors Piece")

        scissors_piece = Scissors.create()
        self.assertIsInstance(scissors_piece, Scissors_Piece,
                              "Scissors create did not create Scissors Piece")

        scissors = Rock()
        self.assertRaises(NotImplementedError, scissors.collide)


if __name__ == '__main__':
    unittest.main()
