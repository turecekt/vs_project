"""Main logic of program."""


def is_prime_number(num):
    """Checking if number is prime number or not."""
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                return str(num) + " is not prime number."
                break
            else:
                return str(num) + " is prime number."
                break


def check_input(user_input):
    """Check if user put allowed input."""
    try:
        """Check if input is integer."""
        num = int(user_input)
        return is_prime_number(num)

    except ValueError:
        try:
            """Check if input is float."""
            num = float(user_input)
            return is_prime_number(num)

        except ValueError:
            """This is not number at all error."""
            return "This is not a number!"
