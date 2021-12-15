Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# Dictionary representing the morse code chart
import pytest

MORSE_CODE_DICT = { '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
 
# Function to decrypt the string
# from morse to english
# Hard-coded driver function to run the program
def main():
    message = input("Zadaj nieco: ")
    result = encrypt(message.upper())
    print (result)
 
    message = "-.. .- -. .. . .-.. ...- .- ... -.- ---"
    result = decrypt(message)
    print (result)
 
# Executes the main function
if __name__ == '__main__':
    main()

def test_answer():
    assert encrypt("35") == "...-- ..... "

def test_answer2():
    assert encrypt("A") == ".- "

def test_answer3():
    assert encrypt("A35") == ".- ...-- ..... "
   

    
[DEBUG ON]
[DEBUG OFF]
encrytp("123")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    encrytp("123")
NameError: name 'encrytp' is not defined
