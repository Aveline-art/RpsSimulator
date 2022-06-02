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

        rock = Rock()
        self.assertRaises(NotImplementedError, rock.collide)

        [rock_piece] = rock.create()
        self.assertIsInstance(rock_piece, Rock_Piece,
                              "Rock create did not create Rock Piece")

        self.assertRaises(ValueError, rock.create, num=0)
        self.assertRaises(ValueError, rock.create, num=-1)
        self.assertRaises(ValueError, rock.create, num=-1000)
        rock.create(num=29)
        self.assertGreater(len(rock.group), 29,
                           "There should be more than 29 sprites in rock group \
                           since 1 was added previously")

    def test_paper(self):
        self.assertIsInstance(Paper.piece(), Paper_Piece,
                              "Paper piece is not Paper Piece")

        paper = Paper()
        self.assertRaises(NotImplementedError, paper.collide)

        [paper_piece] = paper.create()
        self.assertIsInstance(paper_piece, Paper_Piece,
                              "Paper create did not create Paper Piece")

    def test_scissors(self):
        self.assertIsInstance(Scissors.piece(), Scissors_Piece,
                              "Scissors piece is not Scissors Piece")

        scissors = Scissors()
        self.assertRaises(NotImplementedError, scissors.collide)

        [scissors_piece] = scissors.create()
        self.assertIsInstance(scissors_piece, Scissors_Piece,
                              "Scissors create did not create Scissors Piece")


if __name__ == '__main__':
    unittest.main()
