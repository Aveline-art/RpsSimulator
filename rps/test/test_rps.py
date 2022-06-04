import unittest
from rps.pieces import Rock_Piece
from rps.rps import RPS


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

        self.assertEqual(rps.directions['SO'],
                         (0, 5), "North should move (0, 5)")
        self.assertEqual(rps.directions['NE'],
                         (5, -5), "North should move (5, -5)")
        self.assertEqual(rps.directions['CE'],
                         (0, 0), "North should move (0, 0)")

        def move(itself):
            move_center_before_move = itself.rect.center
            self.assertEqual(move_center_before_move, (200, 200),
                             "Move function should have a(it)self object when\
                             prototyped.")
            return (0, -6)

        rps.prototype_move(move)

        [sprite] = rps.rock.create((200, 200))
        self.assertEqual(sprite.rect.center, (200, 200),
                         "Center should be (200, 200)")
        sprite.move()
        self.assertEqual(sprite.rect.center, (200, 194),
                         "Center should be down 6 pixels.")


if __name__ == '__main__':
    unittest.main()
