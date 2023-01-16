"""This is the test of projekt.py."""
from projekt import is_prime, primes_sieve


def test_is_prime():
    """This is test function of is_prime."""
    assert is_prime(73939133)
    assert not is_prime(228)
    assert not is_prime(-10)


def test_primes_sieve():
    """This is test function of prime_sieve."""
    assert not primes_sieve(6)
    assert not primes_sieve(-12)
    assert primes_sieve(67)
