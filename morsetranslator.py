import unittest
"""morsetranslator.py - your daily morse translator"""

"""Slovník morseovy abecedy"""
morseAlphabet ={
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


"""Metoda pro převod morseovy abecedy na text"""
def decodeMorse(code, positionInString=0):
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


"""Metoda pro převod textu na morseovu abecedu"""
def encodeToMorse(message):
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += morseAlphabet[char.upper()] + " "
    return encodedMessage


"""Hlavní metoda main"""
def main():
    # Návod
    print("===============Morse to text / Text to morse translator===============")
    print("pro převod z morseovy abecedy na text používej . nebo - a za každým písmenem vlož mezeru(i na konec) a pro mezery mezi slovy použij /")
    print("pro převod z textu na morseovu abecedu používej latinskou abecedu bez diakritiky a mezery pro oddělení slov")

    # User input (uživatel vloží string pro dekódování/zakódování morseovy abecedy)
    userInput = input ("Vlož morseovu abecedu nebo text pro přeložení: ")
    
    # Pokud detekuje . nebo - ve stringu userInput, tak bude překládat z morseovy abecedy na text, jinak bude enkódovat text do morseovy abecedy
    str = userInput
    if str.find("." or "-")!=-1:
     print(decodeMorse(userInput))
    else:
     print(encodeToMorse(userInput))

  # Unit testy
class TestTestTest(unittest.TestCase):

    # Test převodu z textu na morseovu abecedu
    def test_1(self):
        result = encodeToMorse("TESTtoMORSE")
        self.assertEqual(result, "- . ... - - --- -- --- .-. ... . ")

    # Test převodu z morseovy abecedy na text
    def test_2(self):
        result = decodeMorse("- . ... - - --- -- --- .-. ... . ")
        self.assertEqual(result, "TESTTOMORSE")

if __name__ == '__main__':
    main()
