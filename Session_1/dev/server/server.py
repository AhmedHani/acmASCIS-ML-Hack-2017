___author__ = 'acmASCIS'

'''
    by ahani at {9/26/2016}
'''

import sys
from judge import Judge


def main():
    if len(sys.argv) <= 1:
        raise Exception("Check your arguments please!")

    project_dir = sys.argv[1]
    user_dataset = []

    def get_user_dataset():
        sort_input_path = sys.argv[2]
        sort_output_path = sys.argv[3]
        freq_input_path = sys.argv[4]
        freq_output_path = sys.argv[5]
        matmul_input_path = sys.argv[6]
        matmul_output_path = sys.argv[7]
        user_dataset.append(sort_input_path)
        user_dataset.append(sort_output_path)
        user_dataset.append(freq_input_path)
        user_dataset.append(freq_output_path)
        user_dataset.append(matmul_input_path)
        user_dataset.append(matmul_output_path)
    get_user_dataset()

    server_dataset = []

    def get_server_dataset():
        server_sort_input_file = "./datasets/sorting/sort.in"
        server_sort_output_file = "./datasets/sorting/sort.out"
        server_freq_input_file = "./datasets/freq/freq.in"
        server_freq_output_file = "./datasets/freq/freq.out"
        server_matmul_input_file = "./datasets/matmul/matmul.in"
        server_matmul_output_file = "./datasets/matmul/matmul.out"
        server_dataset.append(server_sort_input_file)
        server_dataset.append(server_sort_output_file)
        server_dataset.append(server_freq_input_file)
        server_dataset.append(server_freq_output_file)
        server_dataset.append(server_matmul_input_file)
        server_dataset.append(server_matmul_output_file)
    get_server_dataset()

    if len(server_dataset) != len(user_dataset):
        raise Exception("User and Server datasets aren't equal size!")



    for i in range(len(server_dataset)):
        judge = Judge(server_dataset[i], user_dataset[i])

        if not judge.check():
            raise Exception("Files ", server_dataset[i], "and", user_dataset[i], "aren't matched!")


    # serialization



if __name__ == '__main__':
    main()