"""Unit Testovani Projekt_Morseovka"""

import unittest
from Projekt_Morseovka import encrypt
from Projekt_Morseovka import decrypt
from Projekt_Morseovka import choice


class Morseovka_Test(unittest.TestCase):
    """
    Unit test - Latin to Morse function
    """
    
    
def test_encrypt_1(self):
    # encrypting a word Morseovka
    assert encrypt("Ondra") == ".../-./-../.-./.- "


    """
    Unit test - Latin to Morse function
    """
    
    
def test_encrypt_2(self):
    # encrypting number Morseovka
    assert encrypt("1234") == ".----/..---/...--/....-"

    """
    Unit test - Morse to Latin function
    """
  

def test_decrypt_1(self):
    # encrypting Morse to Latin Characters
    assert decrypt(".../-./-../.-./.-") == "Ondra"

    """
    Unit test - Morse to Latin Numbers function
    """


def test_decrypt_2(self):
    # encrypting Morse to Latin Numbers
    assert decrypt(".---- ..--- ...-- ....-") == "1234"

    """
    Unit test - Choose translation function
    """
    
    
def test_choice_1(self):
    
    assert choice("1") == "1"
 
