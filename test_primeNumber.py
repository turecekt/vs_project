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
import builtins

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

    def test_is_prime():
        """Function test for isPrimeNumber.

        Parameters:
            - number (int): tested number 5
        Returns:
            - output (str): String printed into console,
            statement if number is prime number
        """
        assert isPrimeNumber(5) == True
        assert isPrimeNumber(6) == False
        assert isPrimeNumber(8) == False

    def test_main():
        """Function test for isPrimeNumber.

        Parameters:
             - number (int): tested number 5
        Returns:
            - output (str): String printed into console,
            statement if number is prime number
        """
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        main()
        assert print_values == ["Vstup musi byt cislo!"]




    def main():
        try:
            cislo = int(input("Zadej cislo: "))
            if isPrimeNumber(cislo):
                print(f"Číslo {cislo} je prvočíslo")
            else:
                print(f"Číslo {cislo}  nie je prvočíslo")
        except Exception:
            print("Vstup musi byt cislo!")


if __name__ == '__main__':
    unittest.main()

# print documentation using pydoc.
# print documentation for class
"""print(TestPrimeNumber.__doc__)"""
