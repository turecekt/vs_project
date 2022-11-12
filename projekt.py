import unittest
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

    for i in primes:
        factors = range(i, tmp, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    if vstup in primes:
        return True
    else:
        return False


def power(a, n, p):
    """
    Insert function description
    :param a:
    :param n:
    :param p:
    :return:
    """

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
    return True


# Try - except block to catch if the user input was incorrect
try:
    # Reading user input and converting it to integer
    vstup = int(input("Please write a number to be checked: "))
    # If input is small number, use deterministic method
    if 1 > vstup <= 10000:
        # If function returns True boolean, the input is prime number
        if primes_sieve(vstup):
            print("Your number is prime.")
        else:
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
    else:
        print("Your number isn't prime.")

except ValueError:
    print("Please enter a whole number.")