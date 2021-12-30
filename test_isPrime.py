"""Unit testy pro program IsPrime."""
from .isPrime import isPrime
import unittest


class PrimesTestCase(unittest.TestCase):
    """Funkce overujici prvocisla."""

    def test_should_be_prime(self):
        """Test s vysledkem JE prvocislo."""
        self.assertEqual(True, isPrime(2))
        self.assertEqual(True, isPrime(3))
        self.assertEqual(True, isPrime(17))
        self.assertEqual(True, isPrime(33391))
        self.assertEqual(True, isPrime(199933))

    def test_should_not_be_prime(self):
        """Test s vysledkem NENI prvocislo."""
        self.assertEqual(False, isPrime(-13))
        self.assertEqual(False, isPrime(-2))
        self.assertEqual(False, isPrime(-1))
        self.assertEqual(False, isPrime(0))
        self.assertEqual(False, isPrime(1))
        self.assertEqual(False, isPrime(4))
        self.assertEqual(False, isPrime(16))
        self.assertEqual(False, isPrime(30))
        self.assertEqual(False, isPrime(35))
        self.assertEqual(False, isPrime(81))
        self.assertEqual(False, isPrime(88))
        self.assertEqual(False, isPrime(121))
        self.assertEqual(False, isPrime
                         (1999331999331999331999331999331999331999331999331999335))

if __name__ == '__main__':
    unittest.main()
