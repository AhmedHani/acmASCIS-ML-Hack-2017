___author__ = 'acmASCIS'

'''
    by ahani at {9/26/2016}
'''

import filecmp


class Judge(object):
    def __init__(self, file1, file2):
        self.__file1 = file1
        self.__file2 = file2

    def get_file1(self):
        return self.__file1

    def get_file2(self):
        return self.__file2

    def check(self):
        return filecmp.cmp(self.__file1, self.__file2)