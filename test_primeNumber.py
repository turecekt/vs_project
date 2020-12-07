import unittest


class TestPrimeNumber(unittest.TestCase):


    def test_fiveIsPrimeNumber(self, ):
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


if __name__ == '__main__':
    unittest.main()
