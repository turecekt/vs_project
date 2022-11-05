# Morse Code Decoder/Encoder
## A very basic application to convert plain text into morse code and vice versa

This application expects a user to first choose to decode or encode morse code.
Based upon the user's choice user then enters either morse code in morse characters seperated by commas or regular text in alphabet letters.

The output is either decoded morse code (output = text in latin) or encoded text (output = morse code).

## Features
- Converts text to morse code.
- Converts morse code to text.

## Tech
This simple application uses two functions:

**def encode(user_input):**
Contains a dictionary of alphabet to morse code.
User input is looped through and compared to dictionary keys.
Individual values are concatenated into a variable which is printed to the terminal.
**parameter:** user input
**return:** Morse code.

**def decode(user_input):**
Contains a dictionary of morse code to alphabet.
User input **in morse code** is made into a list which is then looped through
and compared to dictionary keys.
Individual values are concatenated into a variable which is printed to the terminal.
**:parameter:** user_input
**:return:** Morse code translation - text in latin alphabet.

## Installation

No installation needed, just copy the files and run it.

## License

Free to use application.