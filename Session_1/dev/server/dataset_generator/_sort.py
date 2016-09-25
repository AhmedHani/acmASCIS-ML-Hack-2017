___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import random


class Sort(object):
    def __init__(self, data_size):
        self.__data_size = data_size
        self.__array = []

    def get_data_size(self):
        return self.__data_size

    def get_data(self):
        return self.__array

    def set_data(self, data):
        self.__array = data

    def generate_data(self, min=0, max=10):
        self.__array = [random.Random().randint(min, max) for i in range(self.__data_size)]

        return self.__array


