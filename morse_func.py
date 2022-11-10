"""Module containing functions encode and decode."""

# A dictionary containing the following value pairs:
# key = letter of the alphabet, value = morse sign
alpha_to_morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", " ": "|"
}
# A dictionary containing the following value pairs:
# key = morse sign, value = alphabet letter
morse_to_alpha = dict((v, k) for (k, v) in alpha_to_morse.items())

# Function that converts text into morse code
def encode(user_input):
    """Encode text into morse code.

    Contains a dictionary of alphabet to morse code.
    User input is looped through and compared to dictionary keys.
    Individual values are concatenated into a variable which is
    printed to the terminal.
    :param user_input: String of alphabet.
    :return: Morse code.
    """
    # Empty variable which will be used to store converted text into morse code
    encode_output = ""
    # Looping through the list of letters of the alphabet and
    # getting the corresponding values (morse characters) from the dictionary
    for letter in user_input.upper():
        encode_output += alpha_to_morse.get(letter) + " "
    return encode_output


# Function that converts morse code into text
def decode(user_input):
    """Decode morse code into text.

    Contains a dictionary of morse code to alphabet.
    User input in morse code is made into a list which is
    then looped through and compared to dictionary keys.
    Individual values are concatenated into a variable which is
    printed to the terminal.
    :param user_input: String of morse code.
    :return: Morse code translation.
    """
    # Empty variable which will be used to store converted morse code into text
    decode_output = ""
    # A dictionary containing the following value pairs:
    # key = morse sign, value = alphabet letter
    morse_to_alpha = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z", ".----": "1", "..---": "2", "...--": "3",
        "....-": "4", ".....": "5", "-....": "6", "--...": "7",
        "---..": "8", "----.": "9", "-----": "0", "|": " "
    }
    # Individual morse code characters that are typed in by the user
    # are split upon a space and stored in the code variable
    code = user_input.split(" ")
    # Looping through the list of morse code characters and
    # getting the corresponding values (alphabet letters) from the dictionary
    for sign in code:
        decode_output += morse_to_alpha.get(sign)
    return decode_output
