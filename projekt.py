import unittest
import math
import time

"""
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


def main(vstup):
    try:
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

    except ValueError:
        print("Please enter a positive number!")


if __name__ == '__main__':
    main(int(input("Please enter a number: ")))


def test_is_prime():
    assert is_prime(73939133)
    assert not is_prime(228)
    assert not is_prime(-10)


def test_primes_sieve():
    assert not primes_sieve(6)
    assert not primes_sieve(-12)
    assert primes_sieve(67)


def test_main():
    assert main(13) == ["Your number is prime. Sieve method was used."]
    assert main(40) == ["Your number isn't prime. Sieve method was used."]
    assert main(73939) == ["Your number is prime."]
    assert main(73938) == ["Your number isn't prime."]
    assert main("AAA") == ["Please enter a positive number!"]
    assert main(0) == ["Please enter a positive number!"]
