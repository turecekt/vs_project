morse = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', "&": ".-...", "'": ".----.",
    "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
    ":": "---...", ",": "--..--", "=": "-...-",
    "!": "-.-.--", ".": ".-.-.-", "-": "-....-",
    "+": ".-.-.", '"': ".-..-.", "?": "..--..",
    "/": "-..-."
}

def encrypt(sprava):
    
    zasifruj = ''
    for letter in sprava:
        if letter != ' ':


            zasifruj += morse[letter] + ' '
        else:
           
            zasifruj += ' '

    return zasifruj



def decrypt(sprava):

    global i
    sprava += ' '

    odsifruj = ''
    citext = ''
    for letter in sprava:

  
        if letter != ' ':

        
            i = 0


            citext += letter


        else:

            i += 1


            if i == 2:


                odsifruj += ' '
            else:


                odsifruj += \
                    list(morse.keys())[list(morse.values()).index(citext)]
                citext = ''

    return odsifruj


def main():

    sprava = input("Zadajte text na zakodovanie:")
    result = encrypt(sprava.upper())
    print(result)

    sprava = input("Zadajte text na odkodovanie:")
    result = decrypt(sprava)
    print(result)

if __name__ == '__main__':
    main()
