___author__ = 'acmASCIS'

'''
    by ahani at {9/22/2016}
'''


class DataWriter(object):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__file_extension = '.txt' if self.__file_path.endswith('.out') else '.csv'

    def write_file(self, case, output, n_cases):
        if case is "sort":
            with open(self.__file_path, "wb") as writer:
                for array in output:
                    writer.write(' '.join(map(lambda u: str(u), array)))

        if case is "freq":
            with open(self.__file_path, "wb") as writer:
                for dictionary in output:
                    line = ""
                    for item in dictionary.items():
                        line += item[0] + ":" + item[1]
                        line += " "
                    writer.write(line)

        if case is "matmul":
            with open(self.__file_path, "wb") as writer:
                writer.write(str(n_cases))

                for i in range(n_cases):
                    item = output[i]
                    row_size, col_size, result_matrix = item[0], item[1], item[2]
                    writer.write(str(row_size) + " " + str(col_size))
                    for i in range(row_size):
                        line = ""
                        for j in range(col_size):
                            if j < col_size - 1:
                                line += str(result_matrix[i][j]) + " "
                            else:
                                line += str(result_matrix[i][j])
                        writer.write(line)