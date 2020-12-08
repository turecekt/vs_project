""" Module unit tests .
This module is use for do unit test to each function from primeNumber.py
"""
import unittest
from contextlib import redirect_stdout
from io import StringIO


class TestPrimeNumber(unittest.TestCase):
    """Class for TestingPrimeNumber function primeNumber()"""

    def test_fiveIsPrimeNumber(self, ):
        """Function validates that entered number 5 is prime number
                    Args:
                        number 5
                    Returns:
                        - output - print String
                    """
        number = 5
        number_is_prime_number = True
        for divisor in range(2, number):
            if number % divisor == 0:
                number_is_prime_number = False
                break
        if number_is_prime_number and number > 1:
            vypis = "Číslo 5 je prvočíslo"
            print(f"\n{vypis}")
        else:
            vypis = "Číslo 5 není prvočíslo"
            print(f"\n{vypis} ")

        self.assertEqual(vypis, 'Číslo 5 je prvočíslo')

    def test_tenIsNotPrimeNumber(self, ):
        """Function validates that entered number 10 is not prime number
                            Args:
                                number 10
                            Returns:
                                - output - print String
                            """
        number = 10
        number_is_prime_number = True
        for divisor in range(2, number):
            if number % divisor == 0:
                number_is_prime_number = False
                break
        if number_is_prime_number and number > 1:
            vypis = "Číslo 10 je prvočíslo"
            print(f"\n{vypis}")

        else:
            vypis = "Číslo 10 není prvočíslo"
            print(f"\n{vypis} ")
        self.assertEqual(vypis, 'Číslo 10 není prvočíslo')


class PrintedValues(unittest.TestCase):
    def test_numberOfDivisors(self, ):
        """Function validates the number of dividers

                Args:
                    number

                Returns:
                    - output - number of dividers
                """
        number = 5
        counter = 0

        for divisor in range(1, number + 1):
            if number % divisor == 0:
                counter += 1

        print()
        print('počet deliteľov:', counter)
        self.assertEqual(counter, 2)

    def test_printedValues(self, ):
        """Function validates if after evaluation the divisors are printed into console

                        Args:
                            number

                        Returns:
                            - output - print []
                        """
        out = StringIO()
        with redirect_stdout(out):
            # any calls to print (either here or in a called method)
            # get caught while in this scope
            number = 44
            counter = 0
            print('delitele:', end=' ')
            for divisor in range(1, number + 1):
                if number % divisor == 0:
                    counter += 1
                    print(divisor, end=' ')
            print()
            print('počet deliteľov:', counter)
            print("\n")

        self.assertEqual('delitele: 1 2 4 11 22 44 \npočet deliteľov: 6\n\n\n',
                         out.getvalue())


if __name__ == '__main__':
    unittest.main()
