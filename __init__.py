"""Vzorový kód pro závěrečný projekt předmětu Ap1VS.

.. include:: README.md

Následuje ukázka vzorové funkce.
"""


def compute(x):
    """Funkce počítá výsledek výrazu pro zadaný agrument x.

    :param x: Vstupní parametr x.
    :return: Vrací hodnotu výrazu pro vstupní parametr x.

    >>> compute(3)
    3
    """
    x2 = x * x
    return x2 - 2 * x


if __name__ == '__main__':
    num = int(input('Insert a number:'))
    print(compute(num))
