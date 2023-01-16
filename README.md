
# VS_prvocislo
This file consists of two methods for determination of primality
Firrst is ''primes_sieve()''
Deterministic method of finding a prime number.
Method is more is more suited for creating list of primes.
Second function ''is_prime''
also deterministic function
is designed for faster operation when searching for primality of given number.
Simple timetracker is included for performance measuring.
Python time library is used.

## primes_sieve
This function is implementation of sieve of Eratosthenes algorithm
    for finding all prime numbers up to any given limit.
    List of prime numbers is generated up to the upper limit
    given by the parameter ``limit``.
    Function then tests if ``limit`` is in the generated list.
    :param limit: int
        number that is tested for primality
    :return: bool
        function returns true if parameter limit is prime number
## is_prime

This function test if input variable ``vstup`` is prime number.
    Function reduces number of modulators to save time.
    Python math library needs to imported before deployment of this function.
    :param vstup: int
        number that is tested for primality
    :return: bool
        function returns true if vstup is primal number






## Authors

- [@konj27](https://github.com/konj27)

- [@ErikJukin](https://github.com/ErikJukin)

- [@MartinStritesky](https://github.com/MartinStritesky)

- [@Michael00CZ](https://github.com/Michael00CZ)

