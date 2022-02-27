"""morsetranslator.py - your daily morse translator."""
import unittest

"""Slovník morseovy abecedy"""
morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
    }

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())


def decodeMorse(code, positionInString=0):
    """Metoda pro převod morseovy abecedy na text."""
    if positionInString < len(code):
        morseLetter = ""
        for key, char in enumerate(code[positionInString:]):
            if char == " ":
                positionInString = key + positionInString + 1
                letter = inverseMorseAlphabet[morseLetter]
                return letter + decodeMorse(code, positionInString)
            else:
                morseLetter += char
    else:
        return ""


def encodeToMorse(message):
    """Metoda pro převod textu na morseovu abecedu."""
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += morseAlphabet[char.upper()] + " "
    return encodedMessage


def main():
    """Hlavní metoda main."""
    # Návod
    print("======Morse to text / Text to morse translator============")
    print("morse -> text [. ; - ; whitespace ; /]")
    print("za každým písmenem morseovy abecedy udělej mezeru(i na konci)")
    print("text -> morse [A-Z; whitespace]")
    # User input (uživatel vloží string pro dekódování/zakódování)
    userInput = input("Vlož morseovu abecedu nebo text pro přeložení: ")

    # Pokud detekuje . nebo - ve stringu userInput,
    # tak bude překládat z morseovy abecedy na text,
    # jinak bude enkódovat text do morseovy abecedy
    str = userInput
    if str.find("." or "-")!=-1:
        print(decodeMorse(userInput))
    else:
        print(encodeToMorse(userInput))


class TestTestTest(unittest.TestCase):
    """Unit testy."""

    def test_1(self):
        """Test převodu z textu na morseovu abecedu."""
        result = encodeToMorse("TESTtoMORSE")
        self.assertEqual(result, "- . ... - - --- -- --- .-. ... . ")

    def test_2(self):
        """Test převodu z morseovy abecedy na text."""
        result = decodeMorse("- . ... - - --- -- --- .-. ... . ")
        self.assertEqual(result, "TESTTOMORSE")


if __name__ == '__main__':
    main()
