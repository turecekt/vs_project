# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:35:27 2021.

@author: zifca
"""
# Import of necessary packages and modules
from time import perf_counter # Return the value (in fractional seconds)
# of a performance counter
import time # Time acces
import random # Implement pseudo-random number generators for various distributions.
from statistics import mean #Return the sample arithmetic mean
# of data which can be a sequence or iterable.
# import sys


# Short description of the program
def introduction():
    """Script initiation.
    Prints information about this script.
    Prints countdown.
    """
    print('The program generates 5 easy math tasks.'
          '\nReact time and correctness are evaluated. \nGood luck!')
    time.sleep(1)  # Little break of 1s
    print('\nReady!')
    time.sleep(1)  # Little break of 1s
    print('\nSteady!')
    time.sleep(random.randint(1, 4))
    # Break for 2 - 5 sec.
    # Random, so the player must be ready!

    
# Generation of random inputs
def random_inputs():
    ''' Generates integers used in equations.
    '''
    a = random.randint(-10, 10)  # Random integer from interval -10;10
    b = random.randint(-10, 10)  # Random integer from interval -10;10
    sgn = random.choice("+-*/")  # Random sign +, -, * or /
    print('\nWhat is ', a, sgn, b, '?')
    return a, b, sgn # Return a mathematical equation


# Calculation of generated equations - correct results
def calcOfEquations(a, b, sgn):
    """Calculate given equation.
    Calculates generated equations.
    Tests for ilegal operations.

    Returns:
    int: Correct value of equation.
    """
    if sgn == "+":
        correct = a+b # Equation for addition
    elif sgn == "-":
        correct = a-b # Equation for subtraction
    elif sgn == "*":
        correct = a*b # Equation for multiplication
    elif sgn == "/" and b != 0:
        correct = round(a/b, 3) # Equation for division, the divisor cannot be zero
    elif sgn == "/" and b == 0:
        raise ZeroDivisionError('Cannot divide by zero!') # If the divisor is zero, return an error
    return correct


# Final evaluation
def evaluation(results, reactTime):
    ''' Calculate success percentage.
    '''
    success = round(results.count(1)/5*100, 2) # Calculate percentage of successful answers.
    # The correct answers aredivided by the total number and multiplied by 100.
    # The round function returns a number rounded to the nearest 2 decimal place.
    avRate = round(mean(reactTime), 2)  # Return the sample arithmetic mean of react time
    reT = [round(elem, 2) for elem in reactTime]  # Formatted react times
    print('\n \nYour results are:', results,
          '\nOverall success is:', success, ' %')
    print('Details of your react times are:', reT,
          ' s \nMean react time is: ', avRate, ' s')
    return success, avRate, reT

# Termination
# def termination():
    """ After pressing some key, they program will be terminated
    """
    # input('\nDid you enjoy it?') 
    # print('\nThe program will be closed...')
    # time.sleep(1)
    # sys.exit(0)

def user_input():  # Get user input
    return float(input('Vysledek:'))

def question(a, b, sgn):
    correct = calcOfEquations(a, b, sgn)  # Get correct answer
    print('\nWhat is ', a, sgn, b, '?')  # Printout whole equation and ask for answer
    
    t1 = perf_counter()  # Starting point of performace timer

    try:  # if the input is integer, the program executes the 'try' part
        userResult = user_input()  # User inputs his answer
        t2 = perf_counter()  # Endpoint of performace timer
        reactTime = t2 - t1  # Calculates reaction time
        if correct == userResult: # Evaluation of user's answers
            print('Correct')
            result = True
        else:
            print('Wrong')
            result = False
        return result, reactTime

    except ValueError:  # Wrong value given
        t2 = perf_counter()  # Endpoint of performace timer
        print('Wrong input, sorry, good luck with other equations')
        reactTime = t2 - t1  # Calculates reaction time
        result = False  # Result is automatically False/Wrong
    return result, reactTime

# Main function
def myFunction():
    """Contains Main function.

    Main.
    """
    introduction()  # Prints introductory information

    # Creation of list with results (1 for correct, 0 for wrong) initialized with zeros
    results = [0, 0, 0, 0, 0]
    # Creation of list with react times, initialized with zeros
    reactTime = [0, 0, 0, 0, 0]

    for i in range(5):  # Iterates over n-equations
        a, b, sgn = random_inputs()  # Generate parts of equation
        results[i], reactTime[i] = question(a, b, sgn)  # Asks for equation
                                                        # Returns performace result

    # Calculates and prints overall performace evaluation
    evaluation(results, reactTime)

    # termination()  # Termination of the program

if '__main__' == __name__:

    myFunction()  # Calling of the main function that has additional functions
    # This prevents from calling whole script when executing the unit tests
