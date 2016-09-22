___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import unittest
from dataset_generator._freq import Freq


class FreqTest(unittest.TestCase):
    def setUp(self):
        self.__data_size = 4
        self.__freq = Freq(self.__data_size)

    def test_class_creation(self):
        self.assertIsNotNone(self.__freq)

    def test_array_creation(self):
        self.assertIsNotNone(self.__freq.generate_data())

    def test_array_size(self):
        arr = self.__freq.generate_data()
        self.assertEqual(len(arr), self.__data_size)

if __name__ == '__main__':
    unittest.main()