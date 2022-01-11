# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:35:27 2021.

@author: zifca
"""
# Import of necessary packages and modules
from time import perf_counter
import time
import random
from statistics import mean
# import sys


# Short description of the program
def introduction():
    """
    Script initiation.
    
        Prints information about this script.
    
        Prints countdown.
    """
    print('The program generates 5 easy math tasks.'
          '\nReact time and correctness are evaluated. \nGood luck!')
    # Little break of 1s
    time.sleep(1)
    print('\nReady!')
    # Little break of 1s
    time.sleep(1)
    print('\nSteady!')
    # Break for 2 - 5 sec.
    time.sleep(random.randint(1, 4))

    
# Generation of random inputs
def random_inputs():
    """
    Implement random number and sign generators for equations.
        
        Attributes:
            a (int): Random integer from interval -10;10
            b (int): Random integer from interval -10;10
            sgn: Random operator +, -, * or /
            
        Returns:
            a, b, sgn: A mathematical equation
    """
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    sgn = random.choice("+-*/")
    print('\nWhat is ', a, sgn, b, '?')
    return a, b, sgn


# Calculation of generated equations - correct results
def calcOfEquations(a, b, sgn):
    """
    Composes an equation according to the generated sign.
    
    Tests for ilegal operations.

        Returns:
            int: Correct value of equation
    """
    if sgn == "+":
        correct = a+b
    elif sgn == "-":
        correct = a-b
    elif sgn == "*":
        correct = a*b
    elif sgn == "/" and b != 0:
        correct = round(a/b, 3)
    elif sgn == "/" and b == 0:
        raise ZeroDivisionError('Cannot divide by zero!')
    return correct


# Final evaluation
def evaluation(results, reactTime):
    """
    Calculates the overall success.
    
        Parameters:
            result (int): Result of answers
            reactTime (float): Total reaction time
            
        Return:
            success (float): Calculate percentage of successful answers
            avRate (float): Return the sample arithmetic mean of react time
            reT (float): Formatted react times
    """
    success = round(results.count(1)/5*100, 2)
    avRate = round(mean(reactTime), 2)
    reT = [round(elem, 2) for elem in reactTime]
    print('\n \nYour results are:', results,
          '\nOverall success is:', success, ' %')
    print('Details of your react times are:', reT,
          ' s \nMean react time is: ', avRate, ' s')
    return success, avRate, reT


# Termination
# def termination():
    """
    After pressing some key, they program will be terminated.
    """
    # input('\nDid you enjoy it?')
    # print('\nThe program will be closed...')
    # time.sleep(1)
    # sys.exit(0)

    
def user_input():
    """Get user input, return float."""
    return float(input('Vysledek:'))


def question(a, b, sgn):
    """
    Difines answers over time.
    
        Parameters:
            correct (int): Correct value of equation
            t1 (float): Starting point of performace timer
            t2 (float): Endpoint of performace timer
            
        Return:
            result (bool): Evaluation of user's answers
            reactTime (float): Calculates reaction time
    """
    correct = calcOfEquations(a, b, sgn)
    print('\nWhat is ', a, sgn, b, '?')
    t1 = perf_counter()
    
    try:
    """If the input is integer, the program executes the 'try' part."""
        userResult = user_input()
        t2 = perf_counter()
        reactTime = t2 - t1
        if correct == userResult:
            print('Correct')
            result = True
        else:
            print('Wrong')
            result = False
        return result, reactTime
    # Wrong value given
    except ValueError:
        t2 = perf_counter()
        print('Wrong input, sorry, good luck with other equations')
        reactTime = t2 - t1
        result = False
    return result, reactTime

# Main function
def myFunction():
    """
    Contains Main function.
        
    Main.
    """
    # Prints introductory information
    introduction()
    # Creation of list with results (1 for correct, 0 for wrong) initialized with zeros
    results = [0, 0, 0, 0, 0]
    # Creation of list with react times, initialized with zeros
    reactTime = [0, 0, 0, 0, 0]
    
    for i in range(5):
    """
        Iterates over n-equations.
        Generate parts of equation.
        Asks for equation.
        Returns performace result.
    """
        a, b, sgn = random_inputs()
        results[i], reactTime[i] = question(a, b, sgn)
    # Calculates and prints overall performace evaluation
    evaluation(results, reactTime)

    # termination()  # Termination of the program

if '__main__' == __name__:

    myFunction()  # Calling of the main function that has additional functions
    # This prevents from calling whole script when executing the unit tests
