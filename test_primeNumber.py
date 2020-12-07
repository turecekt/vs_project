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


if __name__ == '__main__':
    unittest.main()
