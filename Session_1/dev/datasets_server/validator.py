___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''


class Validator(object):
    @staticmethod
    def validate_custom_sorting_dataset(arrays):
        """
        Check if the arrays are valid for sorting
        :param arrays: (array of arrays) each array contains an array
        :return: Throw an exception if array isn't valid
        """
        for i in range(len(arrays)):
            current_array = arrays[i]

            for i in range(len(current_array)):
                if not str(current_array[i]).isdigit():
                    return False

        return True

    @staticmethod
    def validate_custom_freq_dataset(arrays):
        """
        Check if the arrays are valid for frequencing
        :param arrays: (array of arrays) each array contains an array
        :return: Throw an exception if array isn't valid
        """
        for i in range(len(arrays)):
            current_array = arrays[i]

            for i in range(len(current_array)):
                if not str(current_array[i]).isdigit():
                    raise Exception("Array elements can't be characters at index: " + str(i))

        return True

    @staticmethod
    def validate_custom_matmul_dataset(matrices_list):
        """
        Check if the matrices are valid for multiplication
        :param arrays: (array of tuples) each array contains a tuple that contains key: first matrix value: second matrix (i.e (matrix_a, matrix_b)
        :return: Throw an exception if matrices aren't valid
        """
        idx = 0
        for item in matrices_list:
            matrix_a = item[0]
            matrix_b = item[1]

            if len(matrix_a[0]) != len(matrix_b):
                raise Exception("Matrices aren't compatible at index: " + str(idx))

            idx += 1

        return True

