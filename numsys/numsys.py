def convertToBinary(number): 

    convertedNumber = ""
	remainder = number

	while remainder != 0
		if(remainder % 2 == 0)
			convertedNumber += "0"
		else
			convertedNumber += "1"

		remainder = remainder / 2
  
    return convertedNumber

def convertToOctal(number): 

    convertedNumber = ""
	remainder = number

	while remainder != 0
		if(remainder % 8 == 0)
			convertedNumber += "0"
		if(remainder % 8 == 1)
			convertedNumber += "1"
		if(remainder % 8 == 2)
			convertedNumber += "2"
		if(remainder % 8 == 3)
			convertedNumber += "3"
		if(remainder % 8 == 4)
			convertedNumber += "4"
		if(remainder % 8 == 5)
			convertedNumber += "5"
		if(remainder % 8 == 6)
			convertedNumber += "6"
		if(remainder % 8 == 7)
			convertedNumber += "7"

		remainder = remainder / 8
  
    return convertedNumber

def convertToHexadecimal(number): 

    convertedNumber = ""
	remainder = number

	while remainder != 0
		if(remainder % 16 == 0)
			convertedNumber += "0"
		if(remainder % 16 == 1)
			convertedNumber += "1"
		if(remainder % 16 == 2)
			convertedNumber += "2"
		if(remainder % 16 == 3)
			convertedNumber += "3"
		if(remainder % 16 == 4)
			convertedNumber += "4"
		if(remainder % 16 == 5)
			convertedNumber += "5"
		if(remainder % 16 == 6)
			convertedNumber += "6"
		if(remainder % 16 == 7)
			convertedNumber += "7"
		if(remainder % 16 == 8)
			convertedNumber += "8"
		if(remainder % 16 == 9)
			convertedNumber += "9"
		if(remainder % 16 == 10)
			convertedNumber += "A"
		if(remainder % 16 == 11)
			convertedNumber += "B"
		if(remainder % 16 == 12)
			convertedNumber += "C"
		if(remainder % 16 == 13)
			convertedNumber += "D"
		if(remainder % 16 == 14)
			convertedNumber += "E"
		if(remainder % 16 == 15)
			convertedNumber += "F"

		remainder = remainder / 16
  
    return convertedNumber