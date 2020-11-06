import sys
from argparse import ArgumentParser

def arguments(arg_len):
    # Method for parsing argument from stdin or as parameters
    # Use argparse library
    # Without parameter it read from stdin else from input file
    # return all arguments
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest = "filename", action = "store",
                        help = "Type input FILE", metavar = "FILE")
    if arg_len == 1:
        result = sys.stdin.read()
        return result
    else:
        args = parser.parse_args().filename
        return args

def main():
    arg_length = len(sys.argv)
    input_file = arguments(arg_length)

if __name__ == '__main__':
    main()