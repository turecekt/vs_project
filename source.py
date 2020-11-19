"""Computing numbers.

>>> decr(1)
0

>>> incr(2)
3
>>> incr(4) == 5
True

>>> pwr(4)
16
"""


class Number:
    """Compute numbers."""

    def __init__(self):
        """Construct numbers."""
        if self.__name__ == 'Number':
            print('Numbers')
        elif self.__name__ == 'Numero':
            print('Numero')
        else:
            print('Unknown type')


def incr(x):
    """Increment number."""
    return x + 1


def decr(x):
    """Decrement number."""
    return x - 1


def pwr(x):
    """Power number."""
    return x * x


if __name__ == '__main__':
    print('run test for source')
