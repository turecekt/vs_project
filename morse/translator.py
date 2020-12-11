import time

from chars import letters_to_morse, morse_to_letters


# letters are encoded to morse code
# returns morse code
def encode(letters):
    output = ''
    for i in letters:
        if i not in letters_to_morse:
            print('Data not formatted properly')
            time.sleep(5)
            break
        else:
            output += letters_to_morse[i] + ' '
    return output


# morse code is decoded
# returns decoded text
def decode(morse):
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
