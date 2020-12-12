import re
import sys
from argparse import ArgumentParser
from operator import itemgetter


def arguments():
    """Method for parsing argument from std-in or as parameters.

    Use argparse library.
    Args:
        - input - Input file
    Without parameter it read from std-in else from input files
    Returns:
        all parsed arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", action="store",
                        help="Type input FILE", metavar="FILE")

    arg_len = len(sys.argv)
    if arg_len == 1:
        result = sys.stdin.read()
        return read_file(result, arg_len)
    else:
        args = parser.parse_args().filename
        return read_file(args, arg_len)


def read_file(input_file, arg_len):
    """Method for reading char to specific char.

    Returns:
         data = string which will be working next.
    """
    if arg_len != 1:
        with open(input_file, "rt") as f:
            text = f.read()
            data = text.split('#', 1)[0]
    else:
        data = input_file.split('#', 1)[0]

    return data


def number_char(file_data):
    """Method return length of passing string.

    Returns:
        number_char = number of characters in string
    """
    num_char=len(file_data)

    return num_char


def number_occurence(file_data):
    """Method create list of occurrence without unwanted chars.

    Returns:
        my_list = list of all characters
    """
    my_list = []
    file_data = file_data.lower()
    for char in file_data:
        if re.match('^[a-z]+$', char):
            count = len(re.findall(char, file_data))
            if not tuple((char, count)) in my_list:
                my_list.append(tuple((char, count)))

    return my_list


def print_number_occurence(list):
    """Method for printing results collected and sorted in list.

    Returns:
        Print output to std-out
    """
    for x in list:
        print('Znak \"', x[0], "\" sa v texte nachadza : ", x[1], "krat")
    print("Najcastejsie sa vyskutuje znak: \"",
          max(list, key=itemgetter(1))[0], "\" a pocet vyskytov je: ",
          max(list, key=itemgetter(1))[1])
    print("Najmenej sa vyskutuje znak: \"",
          min(list, key=itemgetter(1))[0], "\" a pocet vyskytov je: ",
          min(list, key=itemgetter(1))[1])


def main():
    file_data=arguments()
    number_char(file_data)
    print_number_occurence(number_occurence(file_data.replace(" ", "")))

if __name__ == '__main__':
    main()
