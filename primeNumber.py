""" Module prime number checker.
This module is use for checking the input
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
    """Class for evaluating whether the entered number is a prime number."""


number = input("Vlož číslo: ")
counter = int

if number.isdigit() and int(number) > 0:
    number = int(number)
    divisors = []
else:
    print("Nebylo zadáno kladné číslo")


def isPrimeNumber():
    """Function validates the entered number is prime number
       according to divisors and modulos

        Args:
            -

        Returns:
            - output - true, false if number is prime number
        """
    isPrimeNumber = True
    for divisor in range(2, number):
        if number % divisor == 0:
            isPrimeNumber = False
            break
    if isPrimeNumber and number > 1:
        print(f"Číslo {number} je prvočíslo")
    else:
        print(f"Číslo {number} není prvočíslo")


def printDivisors():
    """Function counts number of dividors and print them
            Args:
                -
            Returns:
                - output - number of dividors (counter) and
                  printed list of dividors
            """
    counter = 0
    print('delitele:', end=' ')
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            counter += 1
            print(divisor, end=' ')
    print()
    print('počet deliteľov:', counter)


isPrimeNumber()
printDivisors()
