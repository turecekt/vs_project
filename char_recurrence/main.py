import re
import sys
from argparse import ArgumentParser

def arguments():
    # Method for parsing argument from std-in or as parameters
    # Use argparse library
    # Without parameter it read from std-in else from input file
    # return all arguments
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest = "filename", action = "store",
                        help = "Type input FILE", metavar = "FILE")

    arg_len = len(sys.argv)
    if arg_len == 1:
        result = sys.stdin.read()
        return read_file(result, arg_len)
    else:
        args = parser.parse_args().filename
        return read_file(args, arg_len)

def read_file(input_file, arg_len):
    # Method for reading char to specific char #
    # Method return @data (string which will be working next)
    if arg_len != 1:
        with open(input_file, "rt") as f:
            text = f.read()
            data = text.split('#', 1)[0]
    else:
        data = input_file.split('#', 1)[0]

    return data

def number_char(file_data):
    num_char = len(file_data)

    return num_char

def number_occurence(file_data):
    my_list = []
    file_data = file_data.lower()
    for char in file_data:
        if char.isalpha():
            count = len(re.findall(char, file_data))
            if not tuple((char, count)) in my_list:
                my_list.append(tuple((char, count)))

    return my_list

def main():
    file_data  = arguments()
    number_char(file_data)

if __name__ == '__main__':
    main()