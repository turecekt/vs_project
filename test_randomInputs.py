# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 09:35:11 2021

@author: zifca
"""

import unittest
import random
from reakcniRychlost import *
    
class randomInputs(unittest.TestCase):
    def test_random_inputs_abIsInInterval(self):
        a,b,sgn = random_inputs()
        self.assertTrue(-10 <= a,b <= 10)
      
    def test_random_inputs_abIsInteger(self):
        a,b,sgn = random_inputs()
        self.assertTrue(isinstance(a,int)) and self.assertTrue(isinstance(b,int))
 
    def test_sgn(self):
        a,b,sgn = random_inputs()
        self.assertTrue(sgn in ['+','-','*','/'])
   
if __name__ == '__main__':
    unittest.main()
