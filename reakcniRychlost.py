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


# Main function
def myFunction():
    """Contains Main function.

    Main.
    """
    introduction()
    i = 0
    # Creation of list with results (1 for correct, 0 for wrong) initialized with zeros
    results = [0, 0, 0, 0, 0]
    # Creation of list with react times, initialized with zeros
    reactTime = [0, 0, 0, 0, 0]

    while i < 5: # 5 iterations - from 0 to 4 (5 math equations)
        # Return values from random_inputs() function stored in tuple a,b,sgn
        a, b, sgn = random_inputs()

        # Determination of time and results
        t1 = perf_counter()  # Time - start
        try:  # if the input is integer, the program executes the 'try' part
            userResult = float(input('Vysledek:'))  # User inputs his answer
            t2 = perf_counter()  # Time - end
            reactTime[i] = t2 - t1  # Duration from start to end
              
            correct = calcOfEquations(a, b, sgn)
            # Result of calcOfEquations function stored in var correct
            # Ones/zeros are stored in the list results
            if correct == userResult: # Evaluation of user's answers
                print('Correct')
                results[i] = 1
            else:
                print('Wrong')
                results[i] = 0
        
        # Chech the correctness of the answers
        except ValueError: 
            # If the input is not integer, the 'try' part is not executed, 
            # sentence below is printed and the result is automatically set to 0
            print('Wrong input, sorry, good luck with other equations')
            t2 = perf_counter()  # Time - end
            reactTime[i] = t2 - t1  # Duration from start to end
            results[i] = 0  # Result is automatically 0

        i = i + 1  # next iteration

    evaluation(results, reactTime)  # Final evaluation

    # termination()  # Termination of the program

if '__main__' == __name__:

    myFunction()  # Calling of the main function that has additional functions
    # This prevents from calling whole script when executing the unit tests
