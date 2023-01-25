"""
Test for primality.

This file consists of two methods for determination of primality

First is ''primes_sieve()''
Deterministic method of finding a prime number.
Method is more is more suited for creating list of primes.

Second function ''is_prime''
also deterministic function
is designed for faster operation when searching for primality of given number.

Simple timetracker is included for performance measuring.
Python time library is used.
"""

import math


def primes_sieve(limit):
    """
    Input variable vstup greater than 100 is tested for primality.

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
    Input variable vstup lower than 100 is tested for primality.

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


def main(vstup):
    """Choose an algorithm for primality test."""
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
        print("Please enter a positive number!")


if __name__ == '__main__':
    try:
        main(int(input("Please enter a number: ")))
    except ValueError:
        print("Please enter a positive number!")
