import unittest

"""This file consists of two ways of printing out prime numbers
    primes_sieve() function is a heuristic method of finding a prime number
    is_prime function is a deterministic method."""


def primes_sieve(limit):
    limitn = limit+1
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
    if vstup == 2 or vstup == 3:
        return True

    for i in range(2, int(vstup ** 0.5) + 1):
        if vstup % i == 0:
            return False
    return True


try:
    vstup = int(input("Please write a number to be checked: "))

    if vstup >= 100:
        if primes_sieve(vstup):
            print("Your number is prime.")
        else:
            print("Your number isn't prime.")
    elif 100 > vstup > 1:
        if is_prime(vstup):
            print("Your number is prime.")
        else:
            print("Your number isn't prime.")
    else:
        print("Your number isn't prime.")

except ValueError:
    print("Please enter a whole number!")