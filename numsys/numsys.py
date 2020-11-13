def convertToBinary(number):
	convertedNumber = ""
	remainder = number
	while remainder > 0:
		if remainder % 2 == 0:
			convertedNumber = "0" + convertedNumber
		else:
			convertedNumber = "1" + convertedNumber
		remainder = int(remainder / 2)
		print(remainder)

	return convertedNumber

def convertToOctal(number): 
	convertedNumber = ""
	remainder = number
	while remainder > 0:
		if remainder % 8 == 0:
			convertedNumber = "0" + convertedNumber
		if remainder % 8 == 1:
			convertedNumber = "1" + convertedNumber
		if remainder % 8 == 2:
			convertedNumber = "2" + convertedNumber
		if remainder % 8 == 3:
			convertedNumber = "3" + convertedNumber
		if remainder % 8 == 4:
			convertedNumber = "4" + convertedNumber
		if remainder % 8 == 5:
			convertedNumber = "5" + convertedNumber
		if remainder % 8 == 6:
			convertedNumber = "6" + convertedNumber
		if remainder % 8 == 7:
			convertedNumber = "7" + convertedNumber
		remainder = int(remainder / 8)

	return convertedNumber

def convertToHexadecimal(number): 
	convertedNumber = ""
	remainder = number
	while remainder > 0:
		if remainder % 16 == 0:
			convertedNumber = "0" + convertedNumber
		if remainder % 16 == 1:
			convertedNumber = "1" + convertedNumber
		if remainder % 16 == 2:
			convertedNumber = "2" + convertedNumber
		if remainder % 16 == 3:
			convertedNumber = "3" + convertedNumber
		if remainder % 16 == 4:
			convertedNumber = "4" + convertedNumber
		if remainder % 16 == 5:
			convertedNumber = "5" + convertedNumber
		if remainder % 16 == 6:
			convertedNumber = "6" + convertedNumber
		if remainder % 16 == 7:
			convertedNumber = "7" + convertedNumber
		if remainder % 16 == 8:
			convertedNumber = "8" + convertedNumber
		if remainder % 16 == 9:
			convertedNumber = "9" + convertedNumber
		if remainder % 16 == 10:
			convertedNumber = "A" + convertedNumber
		if remainder % 16 == 11:
			convertedNumber = "B" + convertedNumber
		if remainder % 16 == 12:
			convertedNumber = "C" + convertedNumber
		if remainder % 16 == 13:
			convertedNumber = "D" + convertedNumber
		if remainder % 16 == 14:
			convertedNumber = "E" + convertedNumber
		if remainder % 16 == 15:
			convertedNumber = "F" + convertedNumber
		remainder = int(remainder / 16)

	return convertedNumber

def test_convertToBinary():
	assert convertToBinary(20) == "10100"

def test_convertToOctal():
	assert convertToOctal(20) == "24"

def test_convertToHexadecimal():
	assert convertToHexadecimal(185) == "B9"