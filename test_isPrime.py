"""Unit testy pro program IsPrime."""


from hlavniFunkce import isPrime
import unittest


def test_should_be_prime():
    """Test s vysledkem JE prvocislo."""
    assert isPrime(3) == True
    assert isPrime(7) == True


def test_should_not_be_prime():
    """Test s vysledkem NENI prvocislo."""
    assert isPrime(-11) == False
    assert isPrime(0) == False
    assert isPrime(12) == False


if __name__ == '__main__':
    unittest.main()
