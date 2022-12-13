from NumberSystemConverter import integerToRoman
from NumberSystemConverter import romanToInteger


print(str(None).isNumeric())
integer_input = 3999

roman_number = integerToRoman(integer_input)
print(roman_number)


roman_input = "IV"

integer = romanToInteger(roman_input)
print(integer)
