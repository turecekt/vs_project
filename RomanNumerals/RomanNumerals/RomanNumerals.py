from pickle import TRUE
from NumberSystemConverter import integerToRoman
from NumberSystemConverter import romanToInteger
# from NumberSystemConverter import coverage


def userInterface():

    while (TRUE):

        print()
        print("1 - integer to roman")
        print("2 - roman to integer")
        print("0 - exit")

        userInput = input("input: ")

        if (not userInput.isnumeric()):
            print("wrong input")
            continue

        userInput = int(userInput)

        if (userInput == 1):
            integer = int(input("integer = "))
            print("roman   = " + integerToRoman(integer))

        elif (userInput == 2):
            roman = input("roman   = ")
            print("integer = " + str(romanToInteger(roman)))

        elif (userInput == 0):
            return

        else:
            print("wrong input")


userInterface()
