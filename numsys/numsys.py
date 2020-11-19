from os import system, name

class Convertor:

    def __init__(self):
        clear()
        print("Welcome in math dimensions convertor \n")

        end = False
        while end == False:
            print("Choose numeric dimension into which")
            print("you'd like to convert your number")
            print("1 - Binary")
            print("2 - Octal")
            print("3 - Hexadecimal")
            print("4 - Exit")

            userInput = input()

            if userInput == "1":
                print("Type in number you'd like to convert to binary: ")
                print(convertToBinary(int(input())))

            elif userInput == "2":
                print("Type in number you'd like to convert to octal: ")
                print(convertToOctal(int(input())))

            elif userInput == "3":
                print("Type in number you'd like to convert to binary: ")
                print(convertToHexadecimal(int(input())))

            elif userInput == "4":
                end = True
            else:
                print("Wrong input!")
            
            print()
            print()
            

    def convertToBinary(number):
        if number < 0:
            return "number parameter cant be negative"
        if not isinstance(number, int):
            return "number parameter must be round(int)"

        convertedNumber = ""
        remainder = number
        while remainder > 0:
            if remainder % 2 == 0:
                convertedNumber = "0" + convertedNumber
            else:
                convertedNumber = "1" + convertedNumber
            remainder = int(remainder / 2)

        return convertedNumber



    def convertToOctal(number):
        if number < 0:
            return "number parameter cant be negative"
        if not isinstance(number, int):
            return "number parameter must be round(int)"

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
        if number < 0:
            return "number parameter cant be negative"
        if not isinstance(number, int):
            return "number parameter must be round(int)"

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


    def clear():
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")


    def test_convertToBinary():
        assert convertToBinary(20) == "10100"


    def test_convertToBinaryNegativeParameter():
        assert convertToBinary(-20) == "number parameter cant be negative"


    def test_convertToBinaryParameterNotRound():
        assert convertToBinary(20.5) == "number parameter must be round(int)"


    def test_convertToOctal():
        assert convertToOctal(20) == "24"


    def test_convertToOctalNegativeParameter():
        assert convertToOctal(-20) == "number parameter cant be negative"


    def test_convertToOctalParameterNotRound():
        assert convertToBinary(20.5) == "number parameter must be round(int)"


    def test_convertToHexadecimal():
        assert convertToHexadecimal(185) == "B9"


    def test_convertToHexadecimalNegativeParameter():
        assert convertToHexadecimal(-20) == "number parameter cant be negative"


    def test_convertToHexadecimalParameterNotRound():
        assert convertToBinary(20.5) == "number parameter must be round(int)"

convertor = Convertor()