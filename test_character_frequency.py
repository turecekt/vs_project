#!/usr/bin/env python3

#############################################################################
# Project: AK1VS - Final project
# Description: This project should show how to work with versioning tool such
#              as git.
# Task: Create unittests for chosen project.
#############################################################################
# UTB Zlin - FAI 2020
# Author: Adam Huspenina

from character_frequency import CharacterFrequency
import unittest

class TestCharacterFrequency(unittest.TestCase):
  #############################################################################
  # This is executed only once.
  @classmethod
  def setUpClass(cls):
    cls.chars = CharacterFrequency("")
    
  #############################################################################
  # This is executed at the end.
  @classmethod
  def tearDownClass(cls):
    pass

  #############################################################################
  # This is executed before every test-case.
  def setUp(self):
    pass

  #############################################################################
  # This is executed after every test-case.
  def tearDown(self):
    pass

if __name__ == '__main__':
  unittest.main()