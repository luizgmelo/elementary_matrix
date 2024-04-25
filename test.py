import unittest
from main import *

class TestElementaryMatrix(unittest.TestCase):


    def test_row_switching(self):
        matrix = [
            [2, 1, 3],
            [4, 2, 2],
            [2, 5, 3],
        ]

        """
        L1 <-> L2
        [4,2,2]
        [2,1,3]
        [2,5,3]
        """
        row_switching(0, 1, matrix)
        self.assertEqual(matrix[0], [4,2,2])
        self.assertEqual(matrix[1], [2,1,3])

        """
        L2 <-> L3
        [4,2,2]
        [2,5,3]
        [2,1,3]
        """
        row_switching(1, 2, matrix)
        self.assertEqual(matrix[1], [2,5,3])
        self.assertEqual(matrix[2], [2,1,3])

        """
        L1 <-> L3
        [2,1,3]
        [2,5,3]
        [4,2,2]
        """
        row_switching(0, 2, matrix)
        self.assertEqual(matrix[0], [2,1,3])
        self.assertEqual(matrix[2], [4,2,2])

        

    def test_row_multiplication(self):
        matrix = [
            [2, 1, 3],
            [4, 2, 2],
            [2, 5, 3],
        ]
        """
        L1 -> 8 * L1
        [16,8,24]
        [4,2,2]
        [2,5,3]
        """
        row_multiplication(0, 8, matrix)
        self.assertEqual(matrix[0], [16,8,24])
        """
        L2 -> 3 * L2
        [16,8,24]
        [12,6,6]
        [2,5,3]
        """
        row_multiplication(1, 3, matrix)
        self.assertEqual(matrix[1], [12,6,6])
        """
        L3 -> 7 * L3
        [16,8,24]
        [12,6,6]
        [14,35,21]
        """
        row_multiplication(2, 7, matrix)
        self.assertEqual(matrix[2], [14,35,21])

    # def test_row_addition(self):


if __name__ == '__main__':
    unittest.main()
