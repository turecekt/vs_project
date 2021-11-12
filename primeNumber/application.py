"""Here application starts."""
from prime_number import check_input

if __name__ == '__main__':
    user_input = input('Zadej číslo: ')

    print("\n")

    print(check_input(user_input))
