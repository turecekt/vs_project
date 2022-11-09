"""Thiss is the "example" module for Ap1VS project.

.. include:: README.md
"""


def compute(x):
    """Functon compute returns the evaluation of expression using argument x.

    :param x: First input parameter.
    :return: Expression value for x.

    >>> compute(3)
    3
    """
    x2 = x * x
    return x2 - 2 * x


if __name__ == '__main__':
    num = int(input('Insert a number:'))
    print(compute(num))
