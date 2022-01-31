"""Unit tests"""
import primeCheck
import unittest
from unittest.mock import patch


"""TestCases"""
class Test(unittest.TestCase):
  """Check method isPrime"""
  @patch('builtins.print')
  def test_isPrime(self, mock_print):
    number = 7;
    approach = 'Deterministic'
    primeCheck.isPrimeAndRepeat(number, approach)
    mock_print.assert_called_with(number, "is a prime number.", approach, "approach.")

  """Check isNotPrime"""
  @patch('builtins.print')
  def test_isNotPrime(self, mock_print):
    number = 8
    approach = 'Deterministic'
    primeCheck.isNotPrimeAndRepeat(number, approach)
    mock_print.assert_called_with(number, "is not a prime number.", approach, "approach.")

  """Check method isInteger"""
  def test_isInteger(self):
    self.assertEqual(primeCheck.isInteger(8), True)

  """Check method isNotInteger"""
  def test_isNotInteger(self):
    self.assertEqual(primeCheck.isInteger('AA'), False)

  """Check program with input 7"""
  def test_prime(self):
    self.assertEqual(primeCheck.start(7), 'PRIME')

  """Check program with input 8"""
  def test_notPrime(self):
    self.assertEqual(primeCheck.start(8), 'NOT PRIME')

  """Check method isNotValidInput"""
  @patch('builtins.print')
  def test_isNotValidInput(self, mock_print):
    primeCheck.start('')
    mock_print.assert_called_with('Not valid input')

  """Check if input is zero"""
  @patch('builtins.print')
  def test_isZero(self, mock_print):
    primeCheck.start(0)
    mock_print.assert_called_with('0 is not a valid input')

if __name__ == '__main__':
    unittest.main()
