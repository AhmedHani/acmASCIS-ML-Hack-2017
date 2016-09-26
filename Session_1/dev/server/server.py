___author__ = 'acmASCIS'

'''
    by ahani at {9/26/2016}
'''

import sys


def main():
    if len(sys.argv) <= 1:
        raise Exception("Check your arguments please!")

    project_dir = sys.argv[1]
    sort_input_path = sys.argv[2]
    sort_output_path = sys.argv[3]
    freq_input_path = sys.argv[4]
    freq_output_path = sys.argv[5]
    matmul_input_path = sys.argv[6]
    matmul_output_path = sys.argv[7]

    # DO Validation and serialization



if __name__ == '__main__':
    main()