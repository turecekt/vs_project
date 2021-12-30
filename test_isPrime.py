"""Unit testy pro program IsPrime."""


from hlavniFunkce import isPrime
import unittest


def test_should_be_prime():
    """Test s vysledkem JE prvocislo."""
    assert(isPrime(3))
    assert(isPrime(7))


def test_should_not_be_prime():
    """Test s vysledkem NENI prvocislo."""
    assert(not isPrime(-11))
    assert(not isPrime(0))
    assert(not isPrime(12))


if __name__ == '__main__':
    unittest.main()
