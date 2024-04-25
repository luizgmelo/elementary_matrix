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

        

    # def test_row_multiplication(self):
    # 
    # def test_row_addition(self):


if __name__ == '__main__':
    unittest.main()
