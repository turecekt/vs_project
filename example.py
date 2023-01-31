"""This is the "example" module.

The example module supplies functions for math computation.
"""


def compute(x: int, y: int) -> int:
    """Expression evaluation.

    Function compute returns the evaluation of expression using arguments.

    :param x: First input parameter.
    :param y: Second input parameter.
    :return: Expression value for x and y.

    >>> compute(1, 2)
    4
    """
    z = y - x
    return x + y + z


if __name__ == '__main__':
    num = int(input('Insert a number:'))
    print(compute(num))
