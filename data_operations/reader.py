___author__ = 'acmASCIS'


class DataReader(object):
    '''
    @:parameter a string that is the file path to the input file
    @:parameter a string that is the file path to the output file

    It only supports the following file extensions:
    for input: .in .txt .csv
    for output: .out .txt .csv
    '''
    def __init__(self, input_file_path, output_file_path):
        self.__input_file_path = input_file_path
        self.__output_file_path = output_file_path

        if input_file_path.endswith('.in'):
            self.__input_file_extension = '.in'
        elif input_file_path.endswith('.txt'):
            self.__input_file_extension = '.txt'
        elif input_file_path.endswith('.csv'):
            self.__input_file_extension = '.csv'
        else:
            raise Exception("Invalid input file format!")

        if output_file_path.endswith('.out'):
            self.__output_file_extension = '.out'
        elif output_file_path.endswith('.txt'):
            self.__output_file_extension = '.txt'
        elif output_file_path.endswith('.csv'):
            self.__output_file_extension = '.csv'
        else:
            raise Exception("Invalid output file format!")

    def __format__(self, *args, **kwargs):
        return super(DataReader, self).__format__(*args, **kwargs)

    def __repr__(self):
        return super(DataReader, self).__repr__()

    def __sizeof__(self):
        return super(DataReader, self).__sizeof__()

    def __setattr__(self, name, value):
        return super(DataReader, self).__setattr__(name, value)

    @classmethod
    def __subclasshook__(cls, subclass):
        return super(DataReader, cls).__subclasshook__(subclass)

    def __delattr__(self, name):
        return super(DataReader, self).__delattr__(name)

    @staticmethod
    def __new__(cls, *more):
        return super(DataReader, cls).__new__(*more)

    def __hash__(self):
        return super(DataReader, self).__hash__()

    def __getattribute__(self, name):
        return super(DataReader, self).__getattribute__(name)

    def __str__(self):
        return super(DataReader, self).__str__()

    def __reduce__(self, *args, **kwargs):
        return super(DataReader, self).__reduce__(*args, **kwargs)

    def __reduce_ex__(self, *args, **kwargs):
        return super(DataReader, self).__reduce_ex__(*args, **kwargs)

    def read(self, case):
        if case is "sorting":
            input_arrays_list = []
            output_arrays_list = []

            if self.__input_file_extension is '.in' or self.__input_file_extension is '.txt':
                with open(self.__input_file_path, 'wb') as reader:
                    content = reader.readall()
                    for line in content:
                        array_elements = line.split(" ")
                        array_elements = map(lambda it: int(it), array_elements)
                        input_arrays_list.append(array_elements)

            if self.__output_file_extension is '.out' or self.__output_file_extension is '.txt':
                with open(self.__output_file_path, 'wb') as reader:
                    content = reader.readall()
                    for line in content:
                        array_elements = line.split(" ")
                        array_elements = map(lambda it: int(it), array_elements)
                        output_arrays_list.append(array_elements)

            return input_arrays_list, output_arrays_list

        '''
        TODO implement the other problems data
        '''






