# importing functions
from morse_func import decode, encode

# Exception responsible for validation of the user input (1 or 2)
try:
    # user chooses to encode or decode morse code
    user_option = int(input("For encoding type (1), for decoding type (2): "))
    if user_option == 1:
        print(encode(input("Please enter your text: ")))
    elif user_option == 2:
        print(decode(input("Please enter morse code: ")))
    else:
        print("Invalid input! Please enter 1 for encoding or 2 for decoding.")
except ValueError:
    print("Please use numbers 1 or 2!")
