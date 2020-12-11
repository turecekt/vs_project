"""Main logic of the morse encoder/decoder."""
import time

from chars import letters_to_morse, morse_to_letters


def encode(letters):
    """Letters are encoded to morse code.

    cycles through all the letters one by one
    sets each morse code for given letter to output variable
    returns morse code that is in the output variable.
    """
    output = ''
    for i in letters:
        if i not in letters_to_morse:
            print('Data not formatted properly')
            time.sleep(5)
            break
        else:
            output += letters_to_morse[i] + ' '
    return output


def decode(morse):
    """Morse code is decoded to text.

    cycles through all the morse codes one by one
    sets each letter for given morse code to output variable
    returns decoded text that is in the output variable.
    """
    words = ''
    output = ''
    for i in morse:
        if i != ' ':
            words = words + i
            if i not in morse_to_letters:
                print('Data not formatted properly')
                time.sleep(5)
                break
        elif i == '/':
            output += morse_to_letters[words] + ' '
        else:
            output += morse_to_letters[words] + ''
            words = ''
    return output
