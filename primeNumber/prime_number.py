"""
testovaci komentar v2
"""


def is_prime_number(num):
    """ ahoj"""
    if num > 1:

        for i in range(2, num):

            if (num % i) == 0:
                return str(num) + " neni prvnocislo"
                break
            else:
                return str(num) + " je prvocislo"
                break
