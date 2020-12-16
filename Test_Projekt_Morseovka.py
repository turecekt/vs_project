# -*- coding: utf-8 -*-
"Unit Testovani Projekt_Morseovka"

import unittest
from Projekt_Morseovka import encrypt
from Projekt_Morseovka import decrypt
from Projekt_Morseovka import choice
from Projekt_Morseovka import main

class Morseovka_Test(unittest.TestCase):

    "Unit Tests"
        
    #Unit test - Latin to Morse function
    def test_encrypt_1(self):
        #encrypting word Morseovka
        source = source.encrypt("Morseovka")
        self.assertEqual(vstup, "- . ... - ")

