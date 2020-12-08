import unittest


class TestPrimeNumber(unittest.TestCase):

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
            print(f"{vypis}")
            print("\n")
        else:
            vypis = "Číslo 5 není prvočíslo"
            print(f"{vypis} ")
            print("\n")
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
            print(f"{vypis}")
            print("\n")
        else:
            vypis = "Číslo 10 není prvočíslo"
            print(f"{vypis} ")
            print("\n")
        self.assertEqual(vypis, 'Číslo 10 není prvočíslo')

class PrintedValues(unittest.TestCase):
    def test_numberOfDivisors(self, ):
        """Function validates if after evaluation the divisors are printed into console

                Args:
                    number

                Returns:
                    - output - print []
                """
        number = 5
        counter = 0
        print('delitele:', end=' ')
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                counter += 1
                print(divisor, end=' ')
        print()
        print('\npočet deliteľov:', counter)
        print("\n")
        self.assertEqual(counter, 2)

if __name__ == '__main__':
    unittest.main()
