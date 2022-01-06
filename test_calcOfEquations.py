# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:07:17 2021
@author: zifca
"""

import unittest
import random
from reakcniRychlost import *


class calcOfEquationsPlusSign(unittest.TestCase):
    def test_addPositiveNumbers(self):
        actual = calcOfEquations(5,5,'+')
        self.assertEqual(actual,10)
        
    def test_addNegativeNumbers(self):
        actual = calcOfEquations(-5,-5,'+')
        self.assertEqual(actual,-10)
        
    def test_addNegPosNumbers(self):
        actual = calcOfEquations(-5,8,'+')
        self.assertEqual(actual,3)       

    def test_negativeZero(self):
        actual = calcOfEquations(5,-0,'+')
        self.assertEqual(actual,5) 
        
class calcOfEquationsMinusSign(unittest.TestCase):
    def test_subPositiveNumbers(self):
        actual = calcOfEquations(5,5,'-')
        self.assertEqual(actual,0)

    def test_subPositiveNumbers2(self):
        actual = calcOfEquations(5,8,'-')
        self.assertEqual(actual,-3)
        
    def test_subNegNumbers(self):
        actual = calcOfEquations(-8,-3,'-')
        self.assertEqual(actual,-5)        
        
    def test_subNegNumbers2(self):
        actual = calcOfEquations(-3,-8,'-')
        self.assertEqual(actual,5) 
        
    def test_negativeZero(self):
        actual = calcOfEquations(-3,-0,'-')
        self.assertEqual(actual,-3) 
        
class calcOfEquationsMultiplicationSign(unittest.TestCase):
    def test_multiplyPositiveNumbers(self):
        actual = calcOfEquations(5,5,'*')
        self.assertEqual(actual,25)    
        
    def test_multiplyPosNegNumbers(self):
        actual = calcOfEquations(-5,5,'*')
        self.assertEqual(actual,-25)      

    def test_multiplyNegNumbers(self):
        actual = calcOfEquations(-5,-5,'*')
        self.assertEqual(actual,25) 
        
    def test_multiplyZero(self):
        actual = calcOfEquations(0,-5,'*')
        self.assertEqual(actual,0) 
        
class calcOfEquationsDivisionSign(unittest.TestCase):
    def test_dividePositiveNumbers(self):
        actual = calcOfEquations(5,5,'/')
        self.assertEqual(actual,1)    
        
    def test_dividePosNegNumbers(self):
        actual = calcOfEquations(-5,5,'/')
        self.assertEqual(actual,-1)      

    def test_divideNegNumbers(self):
        actual = calcOfEquations(-5,-5,'/')
        self.assertEqual(actual,1) 
        
    def test_divideZero(self):
        actual = calcOfEquations(0,-5,'/')
        self.assertEqual(actual,0) 
        
    def test_divideZeroByZero(self):
        with self.assertRaises(ZeroDivisionError):
            actual = calcOfEquations(0,0,'/')   
        
class calcOfEquationsError(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            actual = calcOfEquations(5,0,'/')         
        


if __name__ == '__main__':
    unittest.main()
