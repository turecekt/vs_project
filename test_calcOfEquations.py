# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:07:17 2021
@author: zifca
"""

import unittest
import random

def calcOfEquations_forTest(a,b,sgn):
    #Calculation of given equation
    if   sgn == "+": correct = a+b
    elif sgn == "-": correct = a-b
    elif sgn == "*": correct = a*b
    elif sgn == "/" and b != 0: correct = round(a/b,3)
    elif sgn == "/" and b == 0: raise ZeroDivisionError('Cannot divide by zero!')
    else: raise ValueError("Unsupported math operation")
    return correct

class calcOfEquationsPlusSign(unittest.TestCase):
    def test_addPositiveNumbers(self):
        actual = calcOfEquations_forTest(5,5,'+')
        self.assertEqual(actual,10)
        
    def test_addNegativeNumbers(self):
        actual = calcOfEquations_forTest(-5,-5,'+')
        self.assertEqual(actual,-10)
        
    def test_addNegPosNumbers(self):
        actual = calcOfEquations_forTest(-5,8,'+')
        self.assertEqual(actual,3)       

    def test_negativeZero(self):
        actual = calcOfEquations_forTest(5,-0,'+')
        self.assertEqual(actual,5) 
        
class calcOfEquationsMinusSign(unittest.TestCase):
    def test_subPositiveNumbers(self):
        actual = calcOfEquations_forTest(5,5,'-')
        self.assertEqual(actual,0)

    def test_subPositiveNumbers2(self):
        actual = calcOfEquations_forTest(5,8,'-')
        self.assertEqual(actual,-3)
        
    def test_subNegNumbers(self):
        actual = calcOfEquations_forTest(-8,-3,'-')
        self.assertEqual(actual,-5)        
        
    def test_subNegNumbers2(self):
        actual = calcOfEquations_forTest(-3,-8,'-')
        self.assertEqual(actual,5) 
        
    def test_negativeZero(self):
        actual = calcOfEquations_forTest(-3,-0,'-')
        self.assertEqual(actual,-3) 
        
class calcOfEquationsMultiplicationSign(unittest.TestCase):
    def test_multiplyPositiveNumbers(self):
        actual = calcOfEquations_forTest(5,5,'*')
        self.assertEqual(actual,25)    
        
    def test_multiplyPosNegNumbers(self):
        actual = calcOfEquations_forTest(-5,5,'*')
        self.assertEqual(actual,-25)      

    def test_multiplyNegNumbers(self):
        actual = calcOfEquations_forTest(-5,-5,'*')
        self.assertEqual(actual,25) 
        
    def test_multiplyZero(self):
        actual = calcOfEquations_forTest(0,-5,'*')
        self.assertEqual(actual,0) 
        
class calcOfEquationsDivisionSign(unittest.TestCase):
    def test_dividePositiveNumbers(self):
        actual = calcOfEquations_forTest(5,5,'/')
        self.assertEqual(actual,1)    
        
    def test_dividePosNegNumbers(self):
        actual = calcOfEquations_forTest(-5,5,'/')
        self.assertEqual(actual,-1)      

    def test_divideNegNumbers(self):
        actual = calcOfEquations_forTest(-5,-5,'/')
        self.assertEqual(actual,1) 
        
    def test_divideZero(self):
        actual = calcOfEquations_forTest(0,-5,'/')
        self.assertEqual(actual,0) 
        
class calcOfEquationsError(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            actual = calcOfEquations_forTest(5,0,'/')         
        


if __name__ == '__main__':
    unittest.main()
