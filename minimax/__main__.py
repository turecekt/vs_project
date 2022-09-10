"""Project Minimax.

Definition of done:
TODO: add dod

# Keep these lines for the sake of DOCOPT cmd line arguments parser
Usage:
    minimax
    minimax <n>...
    minimax -f <value_file>
"""


from docopt import docopt


def main(args):
    """Docstring of a main method."""
    print("Main method")
    print(args)


if __name__ == "__main__":
    args = docopt(__doc__)
    main(args)
