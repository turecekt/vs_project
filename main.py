def main():
    """
    Get user input and check if the input is prime number

    Return None
    """

    print_input()
    text = input()

    while not check_number(text):
        text = input()
        pass

    if(check_prime_number(int(text))):
        print("Je prvočíslo")
    else:
        print("Není prvočíslo")


def print_input():
    """
    Print sentece to user

    Return None
    """

    print('Zadejte číslo k zjíštění, zda je číslo prvočíslo')


def check_number(text: str):
    """
    This function is checking, if the input is Integer return True if is not
    return False

    Return Boolean
    """
    try:
        int(text)
        return True
    except ValueError:
        print('Zadaný vstup není celé číslo.')
        print_input()
        return False


def check_prime_number(number: int):
    """
    Checking if number is prime number

    Return Boolean
    """

    if(number <= 1):
        return False

    if(number == 2):
        return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    main()
