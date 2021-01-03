"""
Testovaci komentar v3.
//
//
"""


def is_prime_number(num):
    """Ahoj."""
    if num > 1:

        for i in range(2, num):
            """Ahoj."""
            if (num % i) == 0:
                return str(num) + " neni prvnocislo"
                break
            else:
                return str(num) + " je prvocislo"
                break
