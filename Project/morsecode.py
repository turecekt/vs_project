"""Translator.

This module will encode alphabet letters into morse code
and decode morse code back into alphabet letters.
"""

# dictionery translating alphabet letters into morse code
Characters = {"A": ".-",
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
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              "0": "-----",
              "?": "..--..",
              ",": "--..--",
              ".": ".-.-.-",
              ";": "-.-.-.",
              "/": "-..-.",
              "=": "-...-",
              "-": "-....-",
              "'": ".----.",
              "(": "-.--.",
              ")": "-.--.-",
              "\"": ".-..-.",
              ":": "---...",
              "_": "..--.-",
              "+": ".-.-.",
              "@": ".--.-."}


def encode_morse(message):
    """Function encode_morse returns encoded_message in morse code.

    Args:
        - message - Input of the function, string in quotation marks

    Returns:
        - encoded_message - Output of the function, message encoded
        into morse code
    """
    print(message)
    encoded_message = ""
    for char in message.upper():
        if char != " ":
            encoded_message += Characters[char] + " "
        else:
            encoded_message += " "
    print(encoded_message)
    return encoded_message


def decode_morse(message):
    """Function decode_morse returns decoded_message in alphabet.

    Args:
        - message - Input of the function, string in quotation marks

    Returns:
        - decoded_message - Output of the function, message decoded
        from morse code into alphabet
    """
    message += " "
    decoded_message = ""
    letter = ""
    space = 0
    for char in message:
        if char != " ":
            letter += char
            space = 0
        else:
            space += 1
            if space > 1:
                # when there are two spaces, we found the end of the word
                # and a space is added to decoded message
                decoded_message += " "
            else:
                for key, value in Characters.items():
                    if letter == value:
                        decoded_message += key
                        letter = ""
    print(decoded_message)
    return decoded_message


def continue_program():
    """Function continue_program asks user for input."""
    print("If you want to translate another message press 1.")
    print("If you want to close the program press 2.")
    x = input()
    if x == "1":
        main()
    elif x == "2":
        return
    else:
        print("Wrong input.")
        continue_program()


def main():
    """Functon main asks user for input to start encoding/decoding."""
    print("For encoding a message press 1.")
    print("For decoding a message press 2.")
    x = input()
    if x == "1":
        print("Write a string that you want to encode into morse.")
        message = input()
        encode_morse(message)
        continue_program()
    elif x == "2":
        print("Write a string that you want to decode from morse.")
        message = input()
        decode_morse(message)
        continue_program()
    else:
        print("Wrong input.")
        main()
    return


if __name__ == "__main__":
    main()
