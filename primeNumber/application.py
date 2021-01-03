from prime_number import is_prime_number

"""
//
//
//
"""

user_input = input("Zadej cislo: ")
print("\n")

try:
    """ahoj"""
    num = int(user_input)
    is_prime_number(num)

except ValueError:
    try:
        """ahoj"""
        num = float(user_input)
        is_prime_number(num)

    except ValueError:
        print("Toto neni cislo")
