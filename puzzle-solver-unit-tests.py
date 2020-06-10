import unittest
from puzzle_functions import find_number, move_up, move_down, move_left, move_right, measure_mean_std_dev
import numpy as np

class FindNumberTestCase(unittest.TestCase):
    def test_number_zero(self):
        test_array = [[5,2,7,3],[9,1,15,4],[10,6,8,12],[13,11,14,0]]
        zero_location = (3,3)
        self.assertEqual(zero_location, find_number(0,test_array))

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

class MeasureStdDev(unittest.TestCase):
    def test_solved(self):
        result_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        input_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        self.assertEqual(0,measure_mean_std_dev(input_array, result_array)["std_dev"])

    def test_one_move_left(self):
        result_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        input_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
        self.assertEqual(np.std([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]), measure_mean_std_dev(input_array, result_array)["std_dev"])

class MeasureMean(unittest.TestCase):
    def test_solved(self):
        result_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        input_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        self.assertEqual(0,measure_mean_std_dev(input_array, result_array)["mean"])

    def test_one_move_left(self):
        result_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        input_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
        self.assertEqual(np.mean([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]), measure_mean_std_dev(input_array, result_array)["mean"])

if __name__ == '__main__':
    unittest.main()
