"""This file consists of two ways of printing out prime numbers
    primes_sieve() function is a heuristic method of finding a prime number"""

def primes_sieve(limit):
    """Functon compute returns evaluation of expression using argument x.
    :param x: First input parameter.
    :return: Expression value for x.
    >>> compute(200)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    
    """
    limitn = limit+1
    primes = [i for i in range(2,limitn)]

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

vstup = input("Please write a number to be checked: ")
vstup_int = int(vstup)
check = primes_sieve(vstup_int)


if vstup_int >= 100:
    if vstup_int in check:
        print("This number is a prime number.")
    else:
        print("This is not a prime number.")
elif vstup_int<100:
    """insert funkce"""
else:
    print("not a number!")
