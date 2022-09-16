"""Project Minimax.

Definition of done:
TODO: add dod

# Keep these lines for the sake of DOCOPT cmd line arguments parser
Usage:
    minimax (q|b|i|m) [-f FILE | NUMBERS]
"""


from docopt import docopt
from modules import sort_methods, number_extractions


def SortMethodSelector(**kwargs):
    if kwargs['q']:
        return sort_methods.quick_sort
    elif kwargs['b']:
        return sort_methods.bubble_sort
    elif kwargs['m']:
        return sort_methods.merge_sort
    elif kwargs['i']:
        return sort_methods.insertion_sort
    else:
        raise ValueError("Couldn't return right function pointer.")


def Sort(vector, callback):
    sortedList = callback(vector)
    return sortedList


def main(args):
    """Docstring of a main method."""
    print("Main method")
    callback = SortMethodSelector(q=args['q'],
                                  i=args['i'],
                                  m=args['m'],
                                  b=args['b'])

    print(f"Callback to a function: {callback}")

    if args['-f']:
        print("Run with file parameter")
        vector = number_extractions.ExtractNumbersFromFile(args['FILE'])
        print(Sort(vector, callback))

    elif args['NUMBERS']:
        print("Run with commandline params")
        vector = number_extractions.ExtractNumbersFromCLI(args['NUMBERS'])
        print(Sort(vector, callback))

    else:
        print("Run automatically with random numbers")
        vector = number_extractions.GenerateRandomVectorLength20()
        print(Sort(vector, callback))


if __name__ == "__main__":
    args = docopt(__doc__)
    main(args)
