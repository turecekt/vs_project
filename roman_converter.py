"""Arabic Numbers to Roman Numerals Converter V1.0.
Created on Sun Nov  1 14:14:51 2020

@author: Ladislav Tomecek

"""

from roman_library import roman_lib

print("Převodník na římská čísla V1.0")
vstup = int(input("Zadej celé číslo: "))
print(roman_lib().toRoman(vstup))