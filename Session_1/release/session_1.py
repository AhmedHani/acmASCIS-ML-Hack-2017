___author__ = 'acmASCIS'

'''
    by ahani at {9/24/2016}
'''
import sys
from datasets_processing.reader import DataReader
from practical._sort import Sort
from practical._freq import Freq
from practical._matmul import Matmul


def main():
    params = {'problem_def': "", "input_file": "", "output_file": ""}

    def set_parameters():
        if len(sys.argv) > 1:
            print "Number of Arguments: ", len(sys.argv), "arguments"
            params['problem_def'] = sys.argv[0]
            params["input_file"] = sys.argv[1]
            params["output_file"] = sys.argv[2]
        else:
            params['problem_def'] = "sort"  # sort || freq || matmul
            params[
                "input_file"] = "./datasets/sorting/sort_1.in"  # sorting ||arrays_multiplication || elements_frequency
            params[
                "output_file"] = "./datasets/sorting/sort_1.out"  # sorting ||arrays_multiplication || elements_frequency
    set_parameters()

    data_reader = DataReader(params["input_file"], params["output_file"])
    data = []

    def get_data():
        input_data,  output = data_reader.read(params['problem_def'])
        data.append(input_data)
        data.append(output)
    get_data()

    if params['problem_def'] is "sort":
        test_cases = data[0]
        output = data[1]

        for array in test_cases:
            _sort = Sort(array)
            sorted_array = _sort.bubble_sort()
            print(sorted_array)
            output.append(sorted_array)
            #Writer

    if params['problem_def'] is "freq":
        test_cases = data[0]
        output = data[1]

        for array in test_cases:
            _freq = Freq(array)
            freq_array = _freq.get_frequency_array()
            print(freq_array)
            output.append(freq_array)
            #Writer

    if params['problem_def'] is "matmul":
        #TODO

    print params['problem_def']

    return 0


if __name__ == '__main__':
    main()