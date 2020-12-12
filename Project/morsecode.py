#dictionery translating alphabet letters into morse code
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
    """Functon encode_morse returns encoded_message in morse code.
    Args:
        - message - Input of the function, string in quotation marks
    Returns:
        - encoded_message - Output of the function, message encoded into morse code
    """
    encoded_message = ""
    for char in message.upper():
        if char != " ":
            encoded_message += Characters[char] + " "
        else:
            encoded_message += " "
    return encoded_message

def decode_morse(message):
    """Functon decode_morse returns decoded_message in alphabet.
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
                #when there are two spaces, we found the end of the word 
                #and a space is added to decoded message
                decoded_message += " "
            else:
                for key, value in Characters.items():
                    if letter == value:
                        decoded_message += key
                        letter = ""
    return decoded_message
    
