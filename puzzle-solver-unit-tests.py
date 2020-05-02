import unittest
from puzzle_functions import find_zero, move_up, move_down, move_left, move_right

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

class MoveDown(unittest.TestCase):
    def test_bottom_row(self):
        test_array = [[5,11,7,3],[9,1,15,4],[10,6,8,12],[13,0,14,2]]
        self.assertEqual(1, move_down(test_array))

    def test_move_down(self):
        test_array = [[5,2,7,3],[9,1,15,4],[10,6,8,0],[13,11,14,12]]
        result_array = [[5,2,7,3],[9,1,15,4],[10,6,8,12],[13,11,14,0]]
        self.assertEqual(result_array, move_down(test_array))

class MoveLeft(unittest.TestCase):
    def test_left_column(self):
        test_array = [[5,11,7,3],[9,1,15,4],[10,6,8,12],[0,13,14,2]]
        self.assertEqual(1, move_left(test_array))

    def test_move_left(self):
        test_array = [[5,2,7,3],[9,1,15,4],[10,6,8,0],[13,11,14,12]]
        result_array = [[5,2,7,3],[9,1,15,4],[10,6,0,8],[13,11,14,12]]
        self.assertEqual(result_array, move_left(test_array))

class MoveRight(unittest.TestCase):
    def test_right_column(self):
        test_array = [[5,11,7,3],[9,1,15,4],[10,6,8,12],[2,13,14,0]]
        self.assertEqual(1, move_right(test_array))

    def test_move_right(self):
        test_array = [[5,2,7,3],[9,1,15,4],[10,6,0,8],[13,11,14,12]]
        result_array = [[5,2,7,3],[9,1,15,4],[10,6,8,0],[13,11,14,12]]
        self.assertEqual(result_array, move_right(test_array))


if __name__ == '__main__':
    unittest.main()
