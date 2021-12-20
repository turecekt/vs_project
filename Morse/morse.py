
"""
Program pro kodovani a dekodovani morseovy abecedy.
Vypracoval: Petr kraus

"""

morseDictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}



def CodeMorse(message):   
    message.upper()        
    code = ''                         
    for letter in message:              
        if letter != ' ':
            code += morseDictionary[letter] + ' '
        else:
            code += ' '

    return code       



def DecodeMorse(message):
    message += ' '               
    deCode = ''                
    tempText = ''                  

    for letter in message:       
        if (letter != ' '):
            i = 0 
            tempText += letter
        else:
            i += 1
            if i == 2:
                deCode += ' '
            else:
                deCode += list(morseDictionary.keys())[list(morseDictionary.values()).index(tempText)]
                tempText = ''
    return deCode         


