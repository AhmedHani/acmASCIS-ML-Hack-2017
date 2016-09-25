___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''

import random
from dataset_generator._sort import Sort
from dataset_generator._matmul import Matmul
from validator import Validator


class Manager(object):
    def __init__(self):
        super(Manager, self).__init__()

    def make_default_sorting_dataset(self, dataset_size=10, array_length=5):
        """
        Make a random generated dataset for checking the sorting algorithm correctness
        :param dataset_size: (int) Number of arrays that would be created
        :param array_length: (int) The array length
        :return: input and output files path the contains the dataset and its empty output file
        """
        file_index = random.Random().randint(0, 10)
        input_file_path = "./datasets/sorting/sort" + str(file_index) + ".in"
        output_file_path = "./datasets/sorting/sort" + str(file_index) + ".out"
        _sort = Sort(array_length)

        with open(input_file_path, "r") as writer:
            for i in range(dataset_size):
                array_sample = _sort.generate_data()
                array_string = ' '.join(array_sample)
                writer.write(array_string)

        return input_file_path, output_file_path

    def make_custom_sorting_dataset(self, arrays):
        """
        Establish the target dataset from the user.
        :param arrays: (array of arrays) each array contains integer elements
        :return: input and output files path the contains the dataset and its empty output file
        """
        Validator.validate_custom_sorting_dataset(arrays)

        file_index = random.Random().randint(0, 10)
        input_file_path = "./datasets/sorting/sort" + str(file_index) + ".in"
        output_file_path = "./datasets/sorting/sort" + str(file_index) + ".out"

        with open(input_file_path, "r") as writer:
            for i in range(len(arrays)):
                _sort = Sort(len(arrays[i]))
                _sort.set_data(arrays[i])
                array_string = ' '.join(arrays[i])
                writer.write(array_string)

        return input_file_path, output_file_path

    def make_default_freq_dataset(self, dataset_size=10, array_length=5):
        """
        Make a random generated dataset for checking the frequency calculation algorithm correctness
        :param dataset_size: (int) Number of arrays that would be created
        :param array_length: (int) The array length
        :return: input and output files path the contains the dataset and its empty output file
        """
        file_index = random.Random().randint(0, 10)
        input_file_path = "./datasets/elements_frequency/freq" + str(file_index) + ".in"
        output_file_path = "./datasets/elements_frequency/freq" + str(file_index) + ".out"
        _sort = Sort(array_length)

        with open(input_file_path, "r") as writer:
            for i in range(dataset_size):
                array_sample = _sort.generate_data()
                array_string = ' '.join(array_sample)
                writer.write(array_string)

        return input_file_path, output_file_path

    def make_custom_freq_dataset(self, arrays):
        """
        Establish the target dataset from the user.
        :param arrays: (array of arrays) each array contains integer elements
        :return: input and output files path the contains the dataset and its empty output file
        """
        Validator.validate_custom_freq_dataset(arrays)

        file_index = random.Random().randint(0, 10)
        input_file_path = "./datasets/elements_frequency/freq" + str(file_index) + ".in"
        output_file_path = "./datasets/elements_frequency/freq" + str(file_index) + ".out"

        with open(input_file_path, "r") as writer:
            for i in range(len(arrays)):
                _sort = Sort(len(arrays[i]))
                _sort.set_data(arrays[i])
                array_string = ' '.join(arrays[i])
                writer.write(array_string)

        return input_file_path, output_file_path

    def make_default_matmul_dataset(self, dataset_size=10, matrix_a_size=(3, 3), matrix_b_size=(3, 3)):
        """
        Make a random generated dataset for checking the matrix multiplication algorithm correctness
        :param dataset_size: (int) an integer that specifies the number of test cases
        :param matrix_a_size: (tuple) that specifies the first matrix size
        :param matrix_b_size:  (tuple) that specifies the second matrix size
        :return: input and output files path the contains the dataset and its empty output file
        """
        file_index = random.Random().randint(0, 10)
        input_file_path = "./datasets/arrays_multipliction/matmul" + str(file_index) + ".in"
        output_file_path = "./datasets/elements_frequency/matmul" + str(file_index) + ".out"

        with open(input_file_path, "r") as writer:
            writer.write(str(dataset_size))
            for i in range(dataset_size):
                matmul = Matmul(matrix_a_size, matrix_b_size)
                matrix_a, matrix_b = matmul.get_matrices()
                writer.write(str(matrix_a_size[0]) + " " + str(matrix_a_size[1]) + " " + str(matrix_b_size[0]) + " " + str(matrix_b_size[1]))

                for i in range(len(matrix_a)):
                    for j in range(len(matrix_a[0])):
                        if j < len(matrix_a[0]) - 1:
                            writer.write(str(matrix_a[i][j]) + " ")
                        else:
                            writer.write(str(matrix_a[i][j]))

                writer.write("")

                for i in range(len(matrix_b)):
                    for j in range(len(matrix_b[0])):
                        if j < len(matrix_b[0]) - 1:
                            writer.write(str(matrix_b[i][j]) + " ")
                        else:
                            writer.write(str(matrix_b[i][j]))

        return input_file_path, output_file_path

    def make_custom_matmul_dataset(self, matrices_list):
        """
        Establish the target dataset from the user.
        :param matrices_list: (array of tuples) each array contains a tuple that contains key: first matrix value: second matrix (i.e (matrix_a, matrix_b)
        :return: input and output files path the contains the dataset and its empty output file
        """
        Validator.validate_custom_matmul_dataset(matrices_list)

        file_index = random.Random().randint(0, 10)
        input_file_path = "./datasets/arrays_multipliction/matmul" + str(file_index) + ".in"
        output_file_path = "./datasets/elements_frequency/matmul" + str(file_index) + ".out"

        with open(input_file_path, "r") as writer:
            writer.write(str(len(matrices_list)))
            for item in matrices_list:
                writer.write(str(len(item[0])) + " " + str(len(item[0][0])) + " " + str(len(item[1])) + " " + str(len(item[1][0])))
                matrix_a = item[0]
                matrix_b = item[1]

                for i in range(len(matrix_a)):
                    for j in range(len(matrix_a[0])):
                        if j < len(matrix_a[0]) - 1:
                            writer.write(str(matrix_a[i][j]) + " ")
                        else:
                            writer.write(str(matrix_a[i][j]))

                writer.write("")

                for i in range(len(matrix_b)):
                    for j in range(len(matrix_b[0])):
                        if j < len(matrix_b[0]) - 1:
                            writer.write(str(matrix_b[i][j]) + " ")
                        else:
                            writer.write(str(matrix_b[i][j]))

        return input_file_path, output_file_path