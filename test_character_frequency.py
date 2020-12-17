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
    ##########################################################################
    # This is executed only once.
    @classmethod
    def setUpClass(cls):
        cls.chars = CharacterFrequency("DEBUG")
        cls.test_dict = {'a':42, 'b':18, 'c':6, '&':1}

    ##########################################################################
    # This is executed at the end.
    @classmethod
    def tearDownClass(cls):
        pass

    ##########################################################################
    # This is executed before every test-case.
    def setUp(self):
        self.chars.char_dict = self.test_dict
        pass

    ##########################################################################
    # This is executed after every test-case.
    def tearDown(self):
        pass

    ##########################################################################
    # Tests if most frequent character could be found.
    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_most_frequency(self):
        self.chars.char_dict['X'] = 100
        result = self.chars.get_most_frequent()
        self.assertEqual(result[1], 100)

    ##########################################################################
    # Tests if least frequent character could be found.
    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_least_frequency(self):
        self.chars.char_dict['X'] = 1
        result = self.chars.get_least_frequent()
        self.assertEqual(result[1], 1)

    ##########################################################################
    # Tests if character with average rate could be found.
    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_average_frequency(self):
        self.chars.char_dict['X'] = 13
        result = self.chars.get_average()
        self.assertEqual(result[0], 15.5)

    ##########################################################################
    # Tests if alphabetic characters with rate could be filtered.
    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_alphabetic_frequency(self):
        self.chars.char_dict['!'] = 13
        result = self.chars.get_alpha_frequency()
        for key in list(result.keys()):
          self.assertTrue(key.isalpha())


if __name__ == '__main__':
  unittest.main()
