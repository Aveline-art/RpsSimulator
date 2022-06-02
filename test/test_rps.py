import unittest
from rps import RPS


class TestRps(unittest.TestCase):

    def test_rps(self):
        rps = RPS()
        rps.create(30)
        self.assertEqual(len(rps.all_sprites), 90,
                         "There should be a total of 90 sprites.")

        self.assertIsInstance(rps.rock.collide(), dict,
                              "Collide should return a dictionary.")


if __name__ == '__main__':
    unittest.main()