# Last changes 23.11.2020
# Morse code coder and decoder

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1",
           "2", "3", "4", "5", "6", "7", "8", "9", " "]

morseCode = [".-|", "-...|", "-.-.|", "-..|", "-|", "...-.|",
             ".--.|", "....|", "..|", ".---|", "-.-|", ".-..|",
             ".--|", "-.|", "---|", ".--.|", "--.-|", ".-.|",
             "...|", "-|", "..-|", "...-|", ".--|", "-..-|",
             "-.--|", "--..|", "-----|", ".----|", "..---|",
             "...--|", "....-|", ".....|", "-....|", "--...|",
             "---..|", "----.|", ""]


# Checking if input is morse code or not
def is_code(letter):

    if letter == "." or letter == "-":
        return True

    else:
        return False


# Converting input in letters to morse code
def convert_to_code(letter):

    global letters

    if letter not in letters:
        return -1

    i = letters.index(letter)
    return morseCode[i]


# Converting morse code input to letters
def convert_to_letter(code):

    global morseCode

    tmp = code.split("|")
    tmp.pop(len(tmp) - 1)

    for x in range(len(tmp)):
        tmp[x] += "|"
        if tmp[x] not in morseCode:
            return -1

        i = morseCode.index(tmp[x])
        tmp[x] = letters[i]

    return tmp


# Unit testing
def unit_test():

    checks = 0
    stringCheck = "sos"
    morseCodeCheck = "...|---|...|"
    checkMorse = []

    morseCodeCheckFinal = convert_to_letter(morseCodeCheck)
    morseCodeCheckFinal = ''.join(morseCodeCheckFinal)

    if stringCheck.upper() == morseCodeCheckFinal:
        checks += 1

    for i in range(len(stringCheck)):
        checkMorse += convert_to_code(stringCheck[i].upper())

    checkMorse = ''.join(checkMorse)

    if checkMorse == morseCodeCheck:
        checks += 1

    if checks == 2:
        return True
    else:
        return False


# Checking if unit test return true
if unit_test():

    code = input("Enter morse code or sentence: ")

    # Checking what is first char in input, if it is . or - it will use convert to letter function
    if is_code(code[0]):
        final = convert_to_letter(code)
        if final == -1 or final == '':
            print("ERROR INVALID INPUT, PLEASE USE THIS SYNTAX "
                  "exp: ...|---|...| for sos")
        else:
            final = ''.join(final)
            print(final)
    # Else it will use convert to code function
    else:
        finalLetter = []
        for i in range(len(code)):

            tmp = convert_to_code(code[i].upper())

            if tmp == -1:
                print("ERROR INVALID INPUT, PLEASE USE THIS SYNTAX "
                      "exp: ...|---|...| for sos")
                break

            else:
                finalLetter += tmp

        finalLetter = ''.join(finalLetter)
        print(finalLetter)
else:
    print("ERROR HAS OCCURRED WHILE UNIT TESTING")
