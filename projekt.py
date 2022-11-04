import unittest

"""This file consists of two ways of printing out prime numbers
    primes_sieve() function is a heuristic method of finding a prime number"""

def primes_sieve(limit):
    
    limitn = limit+1
    primes = [i for i in range(2,limitn)]
    is_prime = False

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    if limit in primes:
        is_prime = True
    else:
        is_prime = False
        
    return is_prime

vstup = input("Please write a number to be checked: ")
vstup_int = int(vstup)
checkbig = primes_sieve(vstup_int)


if vstup_int >= 100:
    if checkbig:
        print("your number is prime")
    else:
        print("your number isn't prime")
elif vstup_int < 100:
    """insert funkce"""
else:
    print("not a number!")
