import unittest
<<<<<<< HEAD
import random
"""This file consists of two ways of printing out prime numbers
    primes_sieve() function is a deterministic method of finding a prime number
    is_prime_prob function is a probabilistic method."""


def primes_sieve(n):
    """
    Insert function description
    :param n:
    :return:
    """
    tmp = n+1
    primes = [i for i in range(2, tmp)]
=======
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
>>>>>>> origin/master

    for i in primes:
        factors = range(i, tmp, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    if vstup in primes:
        return True
    else:
        return False


<<<<<<< HEAD
def power(a, n, p):
    """
    Insert function description
    :param a:
    :param n:
    :param p:
    :return:
    """
=======
"""def is_prime(vstup):
    if vstup == 2 or vstup == 3:
        return True
>>>>>>> origin/master

    # Initializing "res"
    res = 1
    # If "a" is greater than "p", it is set to the modulus of this division
    a = a % p
    # Calculating the "a" to the power of "n"
    while n > 0:
        # If "n" is odd number, subtract 1 from it to make it even
        # and "res"
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            # Calculating the actual mid-result of "a" with making "a" to the power of 2 and taking modulus by "p"
            a = (a ** 2) % p
            # "n" is updated to the nearest whole number after its division by 2, "n" is even
            n = n // 2
    # Function "power" returns the final modulus
    return res % p


def is_prime_prob(n, k):
    """
    Insert function description
    :param n:
    :param k:
    :return:
    """
    # Number of tries the program performs in order to determine if it is prime number or not
    for i in range(k):
        # Assigns random whole number from 2 to n -2
        a = random.randint(2, n - 2)
        # If result from "power" function is not equal to 1, it is most probably not a prime number
        if power(a, n - 1, n) != 1:
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

<<<<<<< HEAD

# Try - except block to catch if the user input was incorrect
try:
    # Reading user input and converting it to integer
=======
t0 = time.time()
try:

>>>>>>> origin/master
    vstup = int(input("Please write a number to be checked: "))
    # If input is small number, use deterministic method
    if 1 > vstup <= 10000:
        # If function returns True boolean, the input is prime number
        if primes_sieve(vstup):
            print("Your number is prime. This was determined by heuristic method.")
        else:
<<<<<<< HEAD
            print("Your number isn't prime.")
    # if input is larger number, use probabilistic method
    elif vstup > 10000:
        # If function returns True boolean, the input is prime number
        # Second parameter is number of tries
        if is_prime_prob(vstup, 10):
            print("Your number is prime.")
        else:
            print("Your number isn't prime.")
    # Taking care of negative number inputs
=======
            print("Your number isn't prime. This was determined by heuristic  method.")
    elif 100 > vstup > 1:
        if is_prime(vstup):
            print("Your number is prime. Deterministic method was used.")
        else:
            print("Your number isn't prime. Deterministic method was used.")
>>>>>>> origin/master
    else:
        print("Your number isn't prime.")

except ValueError:
<<<<<<< HEAD
    print("Please enter a whole number.")
=======
    print("Please enter a whole number!")

t1 = time.time()
print("Time required :", t1 - t0)
>>>>>>> origin/master
