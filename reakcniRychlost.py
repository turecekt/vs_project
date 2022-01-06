# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:35:27 2021

@author: zifca
"""
#Import of necessary packages and modules
from time import perf_counter
import time
import random
from statistics import mean
import sys

#Short description of the program
def introduction():
    print('The program generates 5 easy math tasks.\nReact time and correctness are evaluated. \nGood luck!') 
    time.sleep(1) #Little break of 1s
    print('\nReady!')
    time.sleep(1) #Little break of 1s
    print('\nSteady!')
    time.sleep(random.randint(1,4)) #Break 2 - 5 sec (random, so the player must be ready!)
 
#Generation of random inputs
def random_inputs():
    a = random.randint(-10, 10) #random integer from interval -10;10
    b = random.randint(-10, 10) #random integer from interval -10;10
    sgn = random.choice("+-*/")  #random sign +-*
    print('\nWhat is ',a,sgn,b, '?') #Math equation
    return a, b, sgn

#Calculation of generated equations - correct results    
def calcOfEquations(a,b,sgn):
    #Calculation of given equation
    if   sgn == "+": correct = a+b
    elif sgn == "-": correct = a-b
    elif sgn == "*": correct = a*b
    elif sgn == "/" and b != 0: correct = round(a/b,3)
    elif sgn == "/" and b == 0: raise ZeroDivisionError('Cannot divide by zero!') 
    else: raise ValueError("Unsupported math operation")
    return correct
    
#Final evaluation  
def evaluation(results,reactTime):
    success = round(results.count(1)/5*100,2) #Calculation of percentage success
    avRate = round(mean(reactTime),2) #Calculation of mean react time
    reT = [round(elem, 2) for elem in reactTime] #Formatted react times
    print('\n \nYour results are:',results,'\nOverall success is:',success,' %')
    print('Details of your react times are:',reT,' s \nMean react time is: ',avRate,' s')
    return success, avRate, reT

#Termination
def termination():
    input('\nDid you enjoy it?')
    print('\nThe program will be closed...')
    time.sleep(1)
    sys.exit(0) 
    
#Main function    
def myFunction():
    introduction() 
    i = 0
    results = [0,0,0,0,0] #Creation of list with results (1 for correct, 0 for wrong)
    reactTime = [0,0,0,0,0] #Creation of list with react times, initialized with zeros
    
    while i < 5: #5 iterations - from 0 to 4 (5 math equations)
        a,b,sgn = random_inputs() #Return values from random_inputs() function stored in tuple a,b,sgn
        t1 = perf_counter() #Time - start
        #Handling of errors - what happens if the user inputs wrong character
        try: #if the input is integer, the program executes the 'try' part
            userResult = float(input('Vysledek:')) #User inputs his answer
            t2 = perf_counter() #Time - end
            reactTime[i] = t2 - t1; #Duration from start to end
            correct = calcOfEquations(a,b,sgn) #Result of calcOfEquations function stored in var correct          
            #Evaluation of user's answers. Ones/zeros are stored in the list results
            if correct == userResult:
                print('Correct')
                results[i] = 1
            else:
                print('Wrong')
                results[i] = 0
                
        #If the input is not integer, the 'try' part is not executed, sentence below is printed and the result is automatically set to 0        
        except ValueError: 
            print('Wrong input, sorry, good luck with other equations')
            t2 = perf_counter() #Time - end
            reactTime[i] = t2 - t1; #Duration from start to end
            results[i] = 0 #Result is automatically 0
            
        i = i + 1 # next iteration
    
    evaluation(results,reactTime) #Final evaluation
    
    termination() #Termination of the program
    
if '__main__' == __name__: 
   
    myFunction() #Calling of the main function that has additional functions        
                 #This prevents from calling whole script when executing the unit tests  
        
    
