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
        """
           Class PrimeNumber for evaluating whether the entered number
           is a prime number.
           A class to represent logic how to validate any number and
           print the results.
           ...
           Attributes
           ----------
           number : int
               input from console
           counter : int
               counter of dividors
           dividors : int[]
               list of dividors
           Methods
           -------
           isPrimeNumber():
               Function validates the entered number is prime number
           printDivisors():
                Function prints number of dividers and their values
           """


number = input("Vlož číslo: ")
counter = int

if number.isdigit() and int(number) > 0:
    number = int(number)
    divisors = []
else:
    print("Nebylo zadáno kladné číslo")


def isPrimeNumber():
    """
        Function validates the entered number is prime number
           according to divisors and modulos
            Parameters:
                number (int): Number is input from console
            Returns:
                output (str): String printed into console, statement if number is
                prime number
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
    """Function counts number of dividers and print them
                Parameters:
                    dividers (int[]): List of integers - dividers
                    counter (int): number of dividers
                Returns:
                    output (int): number of dividors (counter) and
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
