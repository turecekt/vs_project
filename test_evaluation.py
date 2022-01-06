# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:15:12 2021

@author: zifca
"""

import unittest
import random
from statistics import mean
from reakcniRychlost import *

class evaluationTestSuccess(unittest.TestCase):
    def test_success_zeros(self):
        results = [0,0,0,0,0]
        reactTime = [3.36, 3.13, 2.55, 2.43, 2.38]
        success, avRate, reT = evaluation(results,reactTime)
        self.assertEqual(success,0)
     
    def test_success_ones(self):
        results = [1,1,1,1,1]
        reactTime = [3.36, 3.13, 2.55, 2.43, 2.38]
        success, avRate, reT = evaluation(results,reactTime)
        self.assertEqual(success,100)        
        

    def test_success(self):
        results = [1,0,0,1,1]
        reactTime = [3.36, 3.13, 2.55, 2.43, 2.38]
        success, avRate, reT = evaluation(results,reactTime)
        self.assertGreater(100, success,None)
        self.assertLess(0, success, None)
        
class evaluationTestAverageRate(unittest.TestCase):
    def test_avRate(self):
        results = [0,0,0,0,0]
        reactTime = [3.36, 3.13, 2.55, 2.43, 2.38]
        success, avRate, reT = evaluation(results,reactTime)
        self.assertEqual(avRate,2.77)
        
    def test_avRate2(self):
        results = [0,0,0,0,0]
        reactTime = [3.36, 3.13, 2.55, 2.43, 2.38]
        success, avRate, reT = evaluation(results,reactTime)
        self.assertNotEqual(avRate, 2.771)        
        
if __name__ == '__main__':
    unittest.main()
