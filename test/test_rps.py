import unittest
from pieces import Rock_Piece
from rps import RPS


class TestRps(unittest.TestCase):

    def test_rps(self):
        rps = RPS()
        rps.create(30)
        self.assertEqual(len(rps.all_sprites), 90,
                         "There should be a total of 90 sprites.")

        self.assertRaises(ValueError, rps.create, num=0)
        self.assertRaises(ValueError, rps.create, num=-1)
        self.assertRaises(ValueError, rps.create, num=-1000)
        self.assertRaises(TypeError, rps.create, num='should return error')

        self.assertIsInstance(rps.rock.collide(), dict,
                              "Collide should return a dictionary.")

        rps.create_loses_to(Rock_Piece)
        self.assertEqual(len(rps.paper.group), 31,
                         "There should be 1 more sprite added for 31 total.")


if __name__ == '__main__':
    unittest.main()
