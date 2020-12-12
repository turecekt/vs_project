"""Morse translator run file."""
from translator import encode, decode

text_for_encoding = "Hello World!"

morse_code = encode(text_for_encoding)
print(morse_code)

back_to_text = decode(morse_code)
print(back_to_text)
