
# A class of functions for converting between number systems.
from ast import parse
from calendar import c
from email.utils import parsedate
from re import L



class NumberSystemConverter :

    # Function for converting integers to Roman numerals.
    # Converts any positive Integer in range from 1 to 3999.
    def integerToRoman(integer) :
        
        # Checks if the input is really an integer in range 1-3999.
        # If not, function returns error message.
        if (not str(integer).isnumeric() or (integer < 1 or integer > 3999)) :
            return "Input must be any positive integer from 1 to 3999."
        
        # If the input passed the check, the function continues.
        else : pass

        # Declaration of the variable "roman", which will represent the value of the input integer in the system of Roman numerals.
        roman = ""

        # Filling variable "roman" with Roman numerals.
        while (integer > 0) :

            if (integer >= 1000) :
                integer -= 1000
                roman += "M"

            elif (integer >= 900) :
                integer -= 900
                roman += "CM"

            elif (integer >= 500) :
                integer -= 500
                roman += "D"

            elif (integer >= 400) :
                integer -= 400
                roman += "CD"

            elif (integer >= 100) :
                integer -= 100
                roman += "C"

            elif (integer >= 90) :
                integer -= 90
                roman += "XC"

            elif (integer >= 50) :
                integer -= 50
                roman += "L"

            elif (integer >= 40) :
                integer -= 40
                roman += "XL"

            elif (integer >= 10) :
                integer -= 10
                roman += "X"

            elif (integer >= 9) :
                integer -= 9
                roman += "IX"

            elif (integer >= 5) :
                integer -= 5
                roman += "V"

            elif (integer >= 4) :
                integer -= 4
                roman += "IV"

            elif (integer >= 1) :
                integer -= 1
                roman += "I"
            
        # Returns value of the input integer in the system of Roman numerals.
        return roman


    def romanToInteger(roman_number) :

        one_character_numbers = [ 'I', 'V', 'X', 'L', 'C', 'D', 'M' ]
        two_character_numbers = [ 'II', 'IV', 'IX', 'XX', 'XL', 'XC', 'CC', 'CD', 'CM', 'MM' ]
        three_character_numbers = [ 'III', 'XXX', 'CCC', 'MMM' ]

        for char in roman_number :
            if (char not in one_character_numbers) :
                return "Obsahuje nepovolene znaky."
            else : pass
        else : pass
        
        """
        for char in one_character_numbers :
            four_same_chars_in_row = char + char + char + char
            if (four_same_chars_in_row in romanNumber) :
                return "Nemuze obsahovat vice nez tri stejne znaky v rade."
            else : pass
        else : pass
        """

        parsed_roman_number = [roman_number[0]]

        i = 1
        while i < len(roman_number) :

            last_number = parsed_roman_number[len(parsed_roman_number) - 1]
            number = roman_number[i]

            if (NumberSystemConverter.valueOf(last_number + number) > 0) :
                parsed_roman_number[len(parsed_roman_number) - 1] = last_number + number

            else :
                parsed_roman_number.append(number)

            i += 1

        """DEBUG"""
        print(parsed_roman_number)
        """_END_"""

        integer = NumberSystemConverter.valueOf(parsed_roman_number[0])
        value_of_highest_usable_number = NumberSystemConverter.getHighestUsableNumberAfter(integer)
        
        i = 1
        while i < len(parsed_roman_number) :
            
            value_of_last_number = NumberSystemConverter.valueOf(parsed_roman_number[i - 1])
            value_of_number = NumberSystemConverter.valueOf(parsed_roman_number[i])

            if (value_of_last_number > value_of_number) :
                if (value_of_highest_usable_number >= value_of_number) :
                    integer += value_of_number
                    value_of_highest_usable_number = NumberSystemConverter.getHighestUsableNumberAfter(value_of_number)

                else :
                    return "Cislo je ve spatnem tvaru."
                    
            
            else :
                return "Cislo je ve spatnem tvaru."

            i += 1
                
        return integer



    def valueOf(roman_number) :
        if   (roman_number ==   'I') : return    1
        elif (roman_number ==  'II') : return    2
        elif (roman_number == 'III') : return    3
        elif (roman_number ==  'IV') : return    4
        elif (roman_number ==   'V') : return    5
        elif (roman_number ==  'IX') : return    9
        elif (roman_number ==   'X') : return   10
        elif (roman_number ==  'XX') : return   20
        elif (roman_number == 'XXX') : return   30
        elif (roman_number ==  'XL') : return   40
        elif (roman_number ==   'L') : return   50
        elif (roman_number ==  'XC') : return   90
        elif (roman_number ==   'C') : return  100
        elif (roman_number ==  'CC') : return  200
        elif (roman_number == 'CCC') : return  300
        elif (roman_number ==  'CD') : return  400
        elif (roman_number ==   'D') : return  500
        elif (roman_number ==  'CM') : return  900
        elif (roman_number ==   'M') : return 1000
        elif (roman_number ==  'MM') : return 2000
        elif (roman_number == 'MMM') : return 3000
        else : return 0


    def getHighestUsableNumberAfter(number) :
        if   (number >= 1000 and number <= 3000) : return 900
        elif (number ==  900) : return  90
        elif (number ==  500) : return 300
        elif (number >=  100 and number <=  400) : return  90
        elif (number ==   90) : return   9
        elif (number ==   50) : return  30
        elif (number >=   10 and number <=   40) : return   9
        elif (number ==    9) : return   0
        elif (number ==    5) : return   3
        elif (number >=    1 and number <=    4) : return   0
        else : return 0