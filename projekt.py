import unittest
import math
import time

"""
This file consists of two ways of printing out prime numbers
primes_sieve() function is a heuristic method of finding a prime number
is_prime function is a deterministic method.
simple timetracker is included for measuring performance of different algorithms    
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


"""def is_prime(vstup):
    if vstup == 2 or vstup == 3:
        return True

    for i in range(2, int(vstup ** 0.5) + 1):
        if vstup % i == 0:
            return False
    return True"""

def is_prime(vstup):
    """
    This function test if ``vstup`` is prime number by modulation of this number.

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
    for i in range(3, 1 + max_div, 2):#If the given number is divisible by any of the numbers from 3 to the square root of the number skipping all the even numon will return False" \
        if vstup % i == 0:
            return False
    return True

t0 = time.time()
try:

    vstup = int(input("Please write a number to be checked: "))

    if vstup >= 100:
        if primes_sieve(vstup):
            print("Your number is prime. This was determined by heuristic method.")
        else:
            print("Your number isn't prime. This was determined by heuristic  method.")
    elif 100 > vstup > 1:
        if is_prime(vstup):
            print("Your number is prime. Deterministic method was used.")
        else:
            print("Your number isn't prime. Deterministic method was used.")
    else:
        print("Your number isn't prime.")

except ValueError:
    print("Please enter a whole number!")

t1 = time.time()
print("Time required :", t1 - t0)
