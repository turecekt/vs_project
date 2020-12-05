"""Prelozeni vstupu do morzeovky nebo abecedy."""

from morzeovka import mor2ab, ab2mor

user_input = input("Zadejte zpravu: ")
try:
    if user_input[0] == "." or user_input[0] == "-":
        print("Prelozeny text:", mor2ab(user_input))
    else:
        print("Prelozeny text:", ab2mor(user_input))
except IndexError:
    print("Nezadan zadny text")
