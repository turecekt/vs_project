"""Package for converting from and to morse code.

.. include:: README.md
"""
# importing functions
from .morse_func import decode, encode


# main function encodes text into morse code
# or decodes morse code into text
def main():
    """Translate from or into morse code.

    Prompts user to enter either 1 or 2, where 1 is for encoding text
    into morse code and 2 is for decoding morse code into text.
    The user's option value is validated and the result is printed out on
    the terminal based on the user's choice.
    :return: Encoded text into morse code or Decoded morse code into text.
    """
    # user chooses to encode or decode morse code
    user_option = (input("For encoding type (1), for decoding type (2): "))
    # If the user inputs 1, the encode function gets executed and printed out
    if user_option == "1":
        print(encode(input("Please enter your text: ")))
    # If the user inputs 2, the decode function gets executed and printed out
    elif user_option == "2":
        print(decode(input("Please enter morse code: ")))
    # If the user inputs invalid entry
    else:
        print("Invalid input! Please enter 1 for encoding or 2 for decoding.")


if __name__ == "__main__":
    main()
