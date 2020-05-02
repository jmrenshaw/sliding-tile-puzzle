import unittest
from puzzle_functions import find_zero, move_up

class FindZeroTestCase(unittest.TestCase):
    def test_find_zero(self):
        test_array = [[5,2,7,3],[9,1,15,4],[10,6,8,12],[13,11,14,0]]
        zero_location = (3,3)
        self.assertEqual(zero_location, find_zero(test_array))

class MoveUp(unittest.TestCase):
    def test_top_row(self):
        test_array = [[5,0,7,3],[9,1,15,4],[10,6,8,12],[13,11,14,2]]
        self.assertEqual(1, move_up(test_array))

    def test_move_up(self):
        test_array = [[5,2,7,3],[9,1,15,4],[10,6,8,12],[13,11,14,0]]
        result_array = [[5,2,7,3],[9,1,15,4],[10,6,8,0],[13,11,14,12]]
        self.assertEqual(result_array, move_up(test_array))

if __name__ == '__main__':
    unittest.main()
