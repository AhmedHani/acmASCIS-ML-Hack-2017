___author__ = 'acmASCIS'

'''
    by ahani at {9/24/2016}
'''
import time

class Matmul(object):
    def __init__(self, matrix_a, matrix_b):
        self.__matrix_a = matrix_a
        self.__matrix_b = matrix_b
        self.__matrix_a_size = (len(matrix_a), len(matrix_a[0]))
        self.__matrix_b_size = (len(matrix_b), len(matrix_b[0]))

        self.__result_matrix = None
        self.__result_matrix_size = None

        self.__running_time = round(time.time() * 1000)

    def get_matrix_a(self):
        return self.__matrix_a

    def get_matrix_b(self):
        return self.__matrix_b

    def get_matrix_a_size(self):
        return self.__matrix_a_size

    def get_matrix_b_size(self):
        return self.__matrix_b_size

    def get_result_matrix(self):
        if self.__result_matrix is None:
            raise Exception("The result matrix is empty, check your function implementation!")

        return self.__result_matrix

    def get_running_time(self):
        return self.__running_time

    def get_result_matrix_size(self):
        if self.__result_matrix_size is None:
            raise Exception("The result matrix is empty, check your function implementation!")

        return self.__result_matrix_size

    def matrix_multiplication(self):
        """
        Implement your matrix multiplication algorithm
        :return: (array of array [matrix]) that contains the resultant of multiplying matrix_a with matrix_b
        """

        #TODO

        self.__result_matrix_size = (len(self.__result_matrix), len(self.__result_matrix[0]))
        self.__running_time = round(time.time() * 1000) - self.__running_time

        return self.__result_matrix


