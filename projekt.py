"""This file consists of two ways of printing out prime numbers
    primes_sieve() function is a heuristic method of finding a prime number"""

def primes_sieve(limit):
    limitn = limit+1
    primes = range(2, limitn)

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

vstup = input("Please write a number to be checked: ")
if vstup>100:
    primes_sieve(vstup)
elif vstup<100:
    """placeholder"""
else:
    print("not a number!")

