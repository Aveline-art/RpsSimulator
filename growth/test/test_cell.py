import unittest
from growth.cell import Cell


class TestCell(unittest.TestCase):
    A = 'A'
    B = 'B'
    C = 'C'

    def test_cell(self):
        cell = Cell(type=self.A, enemies=[self.B, self.C])
        self.assertEqual(cell.type, self.A, "Cell type should be A")
        self.assertNotEqual(
            cell.enemies, [self.A, self.B],
            "Cell enemies should not contain A.")
        self.assertTrue(cell.surrounded(
            [self.B, self.B]), "Cell should be surrounded.")
        self.assertFalse(cell.surrounded(
            [self.A, self.A, self.B]), "Cell should not be surrounded.")
        self.assertTrue(cell.surrounded(
            [self.A, self.A, self.B], 1), "Cell should be surrounded.")


if __name__ == '__main__':
    unittest.main()
