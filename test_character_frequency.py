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
    cls.chars = CharacterFrequency("DEBUG")
    cls.test_dict = { 'a' : 42, 'b' : 18, 'c' : 6, '&' : 12 }
    
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

  #############################################################################
  # Tests if most frequent character could be found.
  #@unittest.skip('Intentionally skipped for development purposes.')
  def test_most_frequency(self):

  #############################################################################
  # Tests if least frequent character could be found.
  #@unittest.skip('Intentionally skipped for development purposes.')
  def test_least_frequency(self):
    return
  #############################################################################
  # Tests if character with average rate could be found.
  #@unittest.skip('Intentionally skipped for development purposes.')
  def test_average_frequency(self):
    return
  #############################################################################
  # Tests if alphabetic characters with rate could be filtered.
  #@unittest.skip('Intentionally skipped for development purposes.')
  def test_alphabetic_frequency(self):
    return


if __name__ == '__main__':
  unittest.main()