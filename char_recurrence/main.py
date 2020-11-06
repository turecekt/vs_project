import sys
import re
from argparse import ArgumentParser

def arguments():
    # Method for parsing argument from stdin or as parameters
    # Use argparse library
    # Without parameter it read from stdin else from input file
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

    if arg_len != 1:
        with open(input_file, "rt") as f:
            text = f.read()
            data = text.split('#', 1)[0]
    else:
        data = input_file.split('#', 1)[0]

    return data


def main():
    file_data  = arguments()

if __name__ == '__main__':
    main()