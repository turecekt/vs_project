def convertToBinary(number): 

    convertedNumber = ""
	remainder = number
	isNumberConverted = false

	while remainder != 0
		if(remainder % 2 == 0)
			convertedNumber += "0"
		else
			convertedNumber += "1"
		remainder = remainder / 2
  
    return convertedNumber