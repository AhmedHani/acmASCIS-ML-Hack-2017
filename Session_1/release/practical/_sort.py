___author__ = 'acmASCIS'

'''
    by ahani at {9/24/2016}
'''

import time


class Sort(object):
    def __init__(self, array):
        self.__array = array
        self.__sorted_array = None
        self.__array_length = len(array)
        self.__running_time = round(time.time() * 1000)

    def get_original_array(self):
        return self.__array

    def get_array_length(self):
        return self.__array_length

    def get_sorted_array(self):
        if self.__sorted_array is None:
            raise Exception("The sorted array is empty, check your bubble sort implementation!")

        return self.__sorted_array

    def get_running_time(self):
        return self.__running_time

    def bubble_sort(self):
        """
        Implement the bubble sort algorithm
        :return: (array) that contains the elements sorted in ascending order
        """

        #TODO


        self.__running_time = round(time.time() * 1000) - self.__running_time

        return self.__sorted_array
