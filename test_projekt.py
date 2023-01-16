from projekt import *


def test_is_prime():
    assert is_prime(73939133)
    assert not is_prime(228)
    assert not is_prime(-10)


def test_primes_sieve():
    assert not primes_sieve(6)
    assert not primes_sieve(-12)
    assert primes_sieve(67)

