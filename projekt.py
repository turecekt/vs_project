"""This file consists of two ways of printing out prime numbers
    primes_sieve() function is a heuristic method of finding a prime number"""

def primes_sieve(limit):
    limitn = limit+1
    primes = [i for i in range(2,limitn)]

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

vstup = input("Please write a number to be checked: ")
vstup_int= int(vstup)
check=primes_sieve(vstup_int)
if vstup_int in check:
    print("This number is a prime number.")
else:
    print("This is not a prime number.")

"""
if vstup_int >= 100:
    if vstup_int in  primes_sieve(vstup_int):
        print("This number is a prime number.")
    else:
        print("This is not a prime number.")
elif vstup_int<100:
else:
    print("not a number!")
"""
