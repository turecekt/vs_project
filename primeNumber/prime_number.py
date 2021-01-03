"""Ahoj."""


def is_prime_number(num):
    """Ahoj."""
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                return str(num) + " neni prvnocislo"
                break
            else:
                return str(num) + " je prvocislo"
                break


def check_input(user_input):
    """Ahoj."""
    try:
        """Ahoj."""
        num = int(user_input)
        return is_prime_number(num)

    except ValueError:
        try:
            """Ahoj."""
            num = float(user_input)
            return is_prime_number(num)

        except ValueError:
            """Ahoj."""
            return "Toto neni cislo"
