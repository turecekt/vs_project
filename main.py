<<<<<<< HEAD
from unidecode import unidecode

=======
>>>>>>> ed136cceceb2f1e1cccb5183bdbe5089af178882
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
<<<<<<< HEAD
            ',', '.', '?', '/', '-', '(', ')', ' ']
=======
            ',', '.', '?', '/', '-', '(', ')']
>>>>>>> ed136cceceb2f1e1cccb5183bdbe5089af178882

morseCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
             '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
             '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
             '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
<<<<<<< HEAD
             '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-', '']


userInput = unidecode(input())

for letter in userInput:
    print(morseCode[alphabet.index(letter.upper())] + "|", end='', flush=True)
=======
             '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']


userInput = input()

for letter in userInput:
    print(morseCode[alphabet.index(letter.upper())])
>>>>>>> ed136cceceb2f1e1cccb5183bdbe5089af178882
