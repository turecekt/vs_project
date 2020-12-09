"""Module prime number checker.

This module is use for checking the input, supplies  functions:
isPrimeNumber(), printDivisors()

"""


# Author:   Barbana Klimekova <b_klimekova@utb.cz>
#           Lucia Kubaskova <l_kubaskova@utb.cz>
#           Tomas_Prikasky <t_prikasky@utb.cz>
#
# Description:  Create a program to evaluate whether the entered number
#               is a prime number.
#               Prime numbers have exactly two divisors, are divisible
#               by only 1 and by themselves.


class PrimeNumber:
    """Class represents logic how to validate number and print the results.

    ...
    Attributes
    ----------
           - number : int
               - input from console
           - counter : int
               counter of dividors
           - dividors : int[]
               - list of dividors
    Methods
    -------
           isPrimeNumber():
               - Function validates the entered number is prime number
           printDivisors():
                - Function prints number of dividers and their values
    """


# define input from console and global variables
number = input("Vlož číslo: ")
counter = int

# validation of console inputs
if number.isdigit() and int(number) > 0:
    number = int(number)
    # if input is valid, create variable dividors - list of int
    divisors = []
else:
    print("Nebylo zadáno kladné číslo")


def isPrimeNumber(number):
    """Count number of dividers and print them.

    Parameters:
        - dividers (int[]): List of integers - dividers
        - counter (int): number of dividers
    Returns:
        - output (int): number of dividors (counter) and
        printed list of dividors
    """
    # logic of prime number evaluation
    isPrimeNumber = True
    for divisor in range(2, number):
        if number % divisor == 0:
            isPrimeNumber = False
            break
    if isPrimeNumber and number > 1:
        print(f"Číslo {number} je prvočíslo")
    else:
        print(f"Číslo {number} není prvočíslo")


def printDivisors(number):
    """Count number of dividers and print them.

    Parameters:
        - dividers (int[]): List of integers - dividers
        - counter (int): number of dividers
    Returns:
        - output (int): number of dividors (counter) and
        printed list of dividors
    """
    # inicialize and define number of divisers as 0 at the beginning
    counter = 0
    print('Delitele:', end=' ')
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            counter += 1
            print(divisor, end=' ')
    print()
    print('Počet deliteľov:', counter)


isPrimeNumber(number)
printDivisors(number)

# print documentation using pydoc.

# print documentation for class
# print(PrimeNumber.__doc__)
# print documentation for function isPrimeNumber
# print(isPrimeNumber.__doc__)
# print documentation for function printDivisors
# print(printDivisors.__doc__)
