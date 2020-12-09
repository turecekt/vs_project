"""Module unit tests.

This module is use for do unit test to each function from primeNumber.py
"""
# Author:   Barbana Klimekova <b_klimekova@utb.cz>
#           Lucia Kubaskova <l_kubaskova@utb.cz>
#           Tomas_Prikasky <t_prikasky@utb.cz>
#
# Description:  Create unit tests to validate units from primeNumber.py
#               Units: functions isPrimeNumber(), printDivisors()
#               TestCases: 1. prime number validation
#                          2. non-prime number validation
#                          3. dividors validation
#                          4. printed outputs validation
import unittest
from contextlib import redirect_stdout
from io import StringIO
from primeNumber import isPrimeNumber
from primeNumber import printDivisors


class TestPrimeNumber(unittest.TestCase):
    """Class TestPrimeNumber for testing function primeNumber().

    ...
    Attributes
    ----------
            - number : int
                - we are testing numbers 5 and 10, 5 as prime number,
                10 as non-prime number
            - vypis: str
                - the string value that is printed as a result into console
    Methods
    -------
            test_fiveIsPrimeNumber(self, ):
                - Function validates that entered number 5 is prime number
            test_tenIsNotPrimeNumber(self, ):
                - Function validates that number 10 is non-prime number
    """

    def test_fiveIsPrimeNumber(self,):
        """Function test for isPrimeNumber.

        Parameters:
            - number (int): tested number 5
        Returns:
            - output (str): String printed into console,
            statement if number is prime number
        """
        out = StringIO()
        with redirect_stdout(out):
            isPrimeNumber(5)
        self.assertEqual('Číslo 5 je prvočíslo\n',
                         out.getvalue())

    def test_tenIsNotPrimeNumber(self,):
        """Function test function isPrimeNumber.

        Parameters:
            - number (int): tested number 10
        Returns:
            - output (str): String printed into console,
            statement if number is prime number
        """
        out = StringIO()
        with redirect_stdout(out):
            isPrimeNumber(10)
        self.assertEqual('Číslo 10 není prvočíslo\n',
                         out.getvalue())


class TestPrintedValues(unittest.TestCase):
    """Class TestPrintedValues for testing function printDivisors().

    ...
    Attributes
    ----------
            - number : int
                - We are testing numbers 5 and 44, 5 for evaluating
                number of divisors and 44 for evaluating values of divisors
            - dividers: int[]
                - List of integers - dividers
            - counter: int
                - Number of dividers

    Methods
    -------
            test_numberOfDivisors(self, ):
                - Function validates the number of dividers
            test_printedValues(self, ):
                - Function validates if after evaluation the
                divisors are printed into console
    """

    def test_numberOfDivisors(self,):
        """Function validates the number of dividers.

        Parameters:
            - number (int): tested number 5
            - counter (int): number of dividers
        Returns:
            - output (int): number of dividers, printed
            statement into console
        """
        out = StringIO()
        with redirect_stdout(out):
            isPrimeNumber(44)
            printDivisors(44)
        self.assertEqual('Číslo 44 není prvočíslo\nDelitele: 1 2 4 11 22 44 '
                         '\nPočet deliteľov: 6\n',
                         out.getvalue())

    def test_printedValues(self,):
        """Function validates if the divisors are printed into console.

        Parameters:
            - out: output from function catch into method scope
            - number (int): tested number 5
            - counter (int): number of dividers
        Returns:
            - output ():  none, function just asserts values
        """


if __name__ == '__main__':
    unittest.main()

# print documentation using pydoc.
# print documentation for class
"""print(TestPrimeNumber.__doc__)"""
