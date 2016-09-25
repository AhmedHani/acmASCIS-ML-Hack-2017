___author__ = 'acmASCIS'

'''
    by ahani at {9/24/2016}
'''

import time


class Freq(object):
    def __init__(self, array):
        self.__array = array
        self.__frequency_dict = {}
        self.__array_length = len(array)
        self.__running_time = round(time.time() * 1000)

    def get_original_array(self):
        return self.__array

    def get_array_length(self):
        return self.__array_length

    def get_frequency_array(self):
        if self.__frequency_dict is None:
            raise Exception("The frequency array is empty, check your function implementation!")

        return self.__frequency_dict

    def get_running_time(self):
        return self.__running_time

    def get_frequency(self):
        """
        Implement your elements frequency algorithm
        :return: (dictionary) that contains key: element in array, value: frequency. Note that your dictionary should be sorted by key!
        """

        #TODO


        self.__running_time = round(time.time() * 1000) - self.__running_time

        return self.__frequency_dict
