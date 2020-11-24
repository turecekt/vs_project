morse_code = {  '1': '.----',   '2': '..---',   '3': '...--', 
                '4': '....-',   '5': '.....',   '6': '-....', 
                '7': '--...',   '8': '---..',   '9': '----.', 
                '0': '-----',   'A':'.-',       'B':'-...', 
                'C':'-.-.',     'D':'-..',      'E':'.', 
                'F':'..-.',     'G':'--.',      'H':'....', 
                'I':'..',       'J':'.---',     'K':'-.-',  
                'L':'.-..',     'M':'--',       'N':'-.', 
                'O':'---',      'P':'.--.',     'Q':'--.-', 
                'R':'.-.',      'S':'...',      'T':'-', 
                'U':'..-',      'V':'...-',     'W':'.--', 
                'X':'-..-',     'Y':'-.--',     'Z':'--..', 
                ', ':'--..--',  '.':'.-.-.-',   '?':'..--..', 
                '/':'-..-.',    '-':'-....-',   '(':'-.--.', 
                ')':'-.--.-',
                }

def into_morse_code(string):
    result = '' 
         for char in string: 
        if char != ' ': 
            result += morse_code[char] + ' '
        else: 
            result += ' '
    return result

def from_morse_code(string):
    string += ' '

    result = ''
    citext = ''
    for char in string:
        if (char != ' '):
            i = 0
            citext += char
        else:
            i += 1
            if i == 2 :
                result += ' '
            else:
                result += list(morse_code.keys())[list(morse_code
                .values()).index(citext)]
                citext = ''
    return result

if __name__ == '__main__': 
    zadani = input("Vyberte akci (1) = Překlad do morseovy abecedy; (2) = Překlad z morseovy abecedy")
    if zadani == "1": 
        string = input("Zadejte zprávu pro přeložení do morseovy abecedy: ")
        result = into_morse_code(string.upper()) 
        print (result) 
    elif zadani == "2": 
        string = input("Zadejte zprávu pro přeložení z morseovy abecedy: ")
        result = from_morse_code(string) 
        print (result) 
    else: 
        print ("nebylo zadané správné číslo. zadejte 1 nebo 2")