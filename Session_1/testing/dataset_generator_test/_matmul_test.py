___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import unittest
from dataset_generator._mat2 import Mat2


class MatmulTest(unittest.TestCase):
    def setUp(self):
        self.__min = 1
        self.__max = 10
        self.__mat_a_size = (3, 3)
        self.__mat_b_size = (3, 3)
        self.__mat_2 = Mat2(self.__mat_a_size, self.__mat_b_size)

    def test_class_creation(self):
        self.assertIsNotNone(self.__mat_2)

    def test_matrix_creation(self):
        mat_a, mat_b = self.__mat_2.get_matrices(self.__min, self.__max)
        self.assertIsNotNone(mat_a)
        self.assertIsNotNone(mat_b)

    def test_matrix_size(self):
        mat_a, mat_b = self.__mat_2.get_matrices(self.__min, self.__max)
        self.assertEqual(self.__mat_2.get_matrix_a_size(), self.__mat_a_size)
        self.assertEqual(self.__mat_2.get_matrix_b_size(), self.__mat_a_size)

    def test_matrix_elements(self):
        mat_a, mat_b = self.__mat_2.get_matrices(self.__min, self.__max)
        for i in range(len(mat_a)):
            for j in range(len(mat_a[0])):
                self.assertTrue(self.__max >= mat_a[i][j] >= self.__min)

        for i in range(len(mat_b)):
            for j in range(len(mat_b[0])):
                self.assertTrue(self.__max >= mat_b[i][j] >= self.__min)

    def test_mul_validation(self):
        mat_a, mat_b = self.__mat_2.get_matrices(self.__min, self.__max)

        self.assertEqual(len(mat_a[0]), len(mat_b))


if __name__ == '__main__':
    unittest.main()