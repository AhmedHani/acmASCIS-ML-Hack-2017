___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import random


class Freq(object):
    def __init__(self, data_size=100):
        self.__data_size = data_size
        self.__array = []

    def get_data_size(self):
        return self.__data_size

    def get_data(self):
        return self.__array

    def generate_data(self, min_=0, max_=10):
        self.__array = [random.Random().randint(min_, max_) for i in range(self.__data_size)]

        return self.__array