___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import unittest
from dataset_generator._mat1 import Mat1


class Mat1Test(unittest.TestCase):
    def setUp(self):
        self.__min = 1
        self.__max = 10
        self.__mat_size = (3, 3)
        self.__mat_1 = Mat1(self.__mat_size)

    def test_class_creation(self):
        self.assertIsNotNone(self.__mat_1)

    def test_matrix_creation(self):
        mat_a = self.__mat_1.get_matrix(self.__min, self.__max)
        self.assertIsNotNone(mat_a)

    def test_matrix_size(self):
        mat_a = self.__mat_1.get_matrix(self.__min, self.__max)
        self.assertEqual(self.__mat_1.get_matrix_a_size(), self.__mat_size)

    def test_matrix_elements(self):
        mat_a = self.__mat_1.get_matrix(self.__min, self.__max)
        for i in range(len(mat_a)):
            for j in range(len(mat_a[0])):
                self.assertTrue(self.__max >= mat_a[i][j] >= self.__min)


if __name__ == '__main__':
    unittest.main()