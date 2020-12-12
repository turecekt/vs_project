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
    encoded_message = ""
    for char in message.upper():
        if char != " ":
            encoded_message += Characters[char] + " "
        else:
            encoded_message += " "
    return encoded_message

def decode_morse(message):
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
                decoded_message += " "
            else:
                for key, value in Characters.items():
                    if letter == value:
                        decoded_message += key
                        letter = ""
    return decoded_message
    
