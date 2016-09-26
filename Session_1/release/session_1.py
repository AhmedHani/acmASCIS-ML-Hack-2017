___author__ = 'acmASCIS'

'''
    by ahani at {9/24/2016}
'''
import sys
from datasets_processing.reader import DataReader
from practical._sort import Sort
from practical._freq import Freq
from practical._matmul import Matmul
from submit import Submit


def main():
    params = {'opt': "", "input_file": "", "output_file": ""}

    def set_parameters():
        if len(sys.argv) > 1:
            print "Number of Arguments: ", len(sys.argv), "arguments"
            params['problem_def'] = sys.argv[0]
            params["input_file"] = sys.argv[1]
            params["output_file"] = sys.argv[2]
        else:
            params['problem_def'] = "sort"  # sort || freq || matmul
            params[
                "input_file"] = "./datasets/sorting/sort.in"  # sorting || matmul || freq
            params[
                "output_file"] = "./datasets/sorting/sort.out"  # sorting || matmul || freq

    set_parameters()

    data_reader = DataReader(params["input_file"], params["output_file"])
    data = []

    def get_data():
        input_data, output = data_reader.read(params['opt'])
        data.append((input_data, output))

    get_data()

    if params['opt'] is "sort":
        test_cases = data[0][0]
        output = data[0][1]

        for array in test_cases:
            _sort = Sort(array)
            sorted_array = _sort.bubble_sort()
            # print(sorted_array)
            output.append(sorted_array)
            #writer

    if params['opt'] is "freq":
        test_cases = data[0][0]
        output = data[0][1]

        for array in test_cases:
            _freq = Freq(array)
            freq_array = _freq.get_frequency_array()
            # print(freq_array)
            output.append(freq_array)
            #writer

    if params['opt'] is "matmul":
        test_cases = data[0][0]
        output = data[0][1]
        n_cases = len(test_cases)

        for case in test_cases:
            matrix_a_size, matrix_b_size, matrix_a, matrix_b = case[0], case[1], case[2], case[3]
            _matmul = Matmul(matrix_a, matrix_b)
            result_matrix = _matmul.matrix_multiplication()
            # print(result_matrix)
            result_matrix_size = (len(result_matrix), len(result_matrix[0]))
            output.append((result_matrix_size[0], result_matrix[1], result_matrix))

            # writer

    if params['opt'] is "submit":
        sort_input_path = "./datasets/sorting/sort.in"
        sort_output_path = "./datasets/sorting/sort.out"
        freq_input_path = "./datasets/freq/freq.in"
        freq_output_path = "./datasets/freq/freq.out"
        matmul_input_path = "./datasets/matmul/matmul.in"
        matmul_output_path = "./datasets/matmul/matmul.out"

        submit = Submit()
        submit.send(sort_input_path, sort_output_path, freq_input_path, freq_output_path, matmul_input_path, matmul_output_path)
        response = submit.recv()

        if response is "OK":
            #Do serialization




    # submitter to the server do the work here. Then server sends the serialized code to the google drive

    return 0


if __name__ == '__main__':
    main()