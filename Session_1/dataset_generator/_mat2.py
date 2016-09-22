___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import random


class Mat2(object):
    def __init__(self, matrix_a_size=(3, 3), matrix_b_size=(3, 3)):
        self.__matrix_a_size = matrix_a_size
        self.__matrix_b_size = matrix_b_size

        self.__matrix_a = []
        self.__matrix_b = []

    def get_matrix_a(self):
        return self.__matrix_a

    def get_matrix_b(self):
        return self.__matrix_b

    def get_matrix_a_size(self):
        return len(self.__matrix_a), len(self.__matrix_a[0])

    def get_matrix_b_size(self):
        return len(self.__matrix_b), len(self.__matrix_b[0])

    def get_matrices(self, min_=0, max_=10):
        self.__matrix_a = [[random.Random().randint(min_, max_) for j in range(self.__matrix_a_size[1])] for i in range(self.__matrix_a_size[0])]
        self.__matrix_b = [[random.Random().randint(min_, max_) for j in range(self.__matrix_b_size[1])] for i in range(self.__matrix_b_size[0])]

        return self.__matrix_a, self.__matrix_b




