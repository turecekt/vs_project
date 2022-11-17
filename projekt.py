import unittest
import math
import time

"""
This file consists of two ways of printing out prime numbers
''primes_sieve()'' function is a deterministic method of finding a prime number.
''primes_sieve()'' is more is more suited for creating list of primes, but for educational purposes is used for numbers lesser than 100.
Second function ''is_prime'' is also deterministic function, but is designed for faster operation when searching for primality of given number.
Simple timetracker is included for measuring performance of different algorithms. Python time library is used by this tracker.
"""
def primes_sieve(limit):
    """
    This function is implementation of sieve of Eratosthenes algorithm for finding all prime numbers up to any given limit.
    List of prime numbers is generated up to the upper limit given by the parameter ``limit``.
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
    This function test if ``vstup`` is prime number by modulation of this number.
    Python math library needs to imported before deployment of this function.

    :param vstup: int
        number that is tested for primality
    :return: bool
        function returns true if vstup is primal number
    """

    if vstup <= 1:#Function is_prime first tests that input variable vstup is equal or bigger than 1
        return False
    if vstup % 2 == 0:
        return vstup == 2 #it will return True if the number is equal to 2 else false

    max_div = math.floor(math.sqrt(vstup))
    for i in range(3, 1 + max_div, 2):#If the given number is divisible by any of the numbers from 3 to the square root of the number skipping all the even numbers, function will return False
        if vstup % i == 0:
            return False
    return True

t0 = time.time()
try:

    vstup = int(input("Please write a number to be checked: "))

    if vstup >= 100:
        if is_prime(vstup) :
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

t1 = time.time()
print("Time required :", t1 - t0)
