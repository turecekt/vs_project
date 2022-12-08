"""Prvocislo.

.. include:: README.md
"""

import unittest
import math
import time


def primes_sieve(limit):

    """
    This function is implementation of sieve of Eratosthenes algorithm
    for finding all prime numbers up to any given limit.
    List of prime numbers is generated up to the upper limit
    given by the parameter ``limit``.
    Function then tests if ``limit`` is in the generated list.

    :param limit: int
        number that is tested for primality
    :return: bool
        function returns true if parameter limit is prime number
    """

    limitn = limit + 1
    primes = [i for i in range(2, limitn)]

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    if limit in primes:
        return True
    else:
        return False


def is_prime(vstup):
    """
    This function test if input variable ``vstup`` is prime number.
    Function reduces number of modulators to save time.
    Python math library needs to imported before deployment of this function.

    :param vstup: int
        number that is tested for primality
    :return: bool
        function returns true if vstup is primal number
    """

    if vstup <= 1:
        return False
    if vstup % 2 == 0:
        return vstup == 2

    max_div = math.floor(math.sqrt(vstup))
    for i in range(3, 1 + max_div, 2):
        if vstup % i == 0:
            return False
    return True



try:

    vstup = int(input("Please write a number to be checked: "))

    if vstup >= 100:
        if is_prime(vstup):
            print("Your number is prime.")
        else:
            print("Your number isn't prime.")
    elif 100 > vstup > 1:
        if primes_sieve(vstup):
            print("Your number is prime. Sieve method was used.")
        else:
            print("Your number isn't prime. Sieve method was used.")
    else:
        print("Your number isn't prime.")

except ValueError:
    print("Please enter a whole number!")

assert vstup(12)== "Your number isn't prime. Sieve method was used."
