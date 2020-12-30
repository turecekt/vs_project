#Znaky pro přeložení klasické abecedy do Morseovy.#
znaky = {' ': '|', 'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ',': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'}

#Definice fuknce překladače do Morseovy abecedy.#

def prelozit_do(text):
    encrypted_text = "" #Definice proměnné.#
    """Překlad jednotlivých znaků klasické abecedy do Morseovy, pomocí
    výše zadefinovaných znaků a následný převod malých písmen na velké."""
    for i in text:
        encrypted_text += znaky[i.upper()] + ' '
    return encrypted_text

#Definice funkce překladače z Morseovy abecedy.#

def prelozit_z(text):
    text += " "
    key_list = list(znaky.keys())
    value_list = list(znaky.values())
    morse = ""
    normal = ""
    #překlad jednotlyvých znaků Morseovy abecedy do klasické abecedy včetně podmínek pro oddělování.#
    for i in text:
        if i != " ":
            morse += i
            space = 0
        else:
            space += 1
            if space == 2:
                normal += " "  
            else:
                normal = normal + key_list[value_list.index(morse)]
                morse = ""
    return normal

#Uživatel pomocí kláves A a B zvolí, jestli chce text přeložit z nebo do Morseovy abecedy.#

if __name__ == '__main__':
    j = input("\nPro překlad do Morseovy abecedy, stiskněte 'A'."
              "\n\nPro překlad z Morseovy abecedy, stiskněte 'B'.\n")

    if j == 'A' or 'a':
        text_to_encrypt = input("Zadejte text, který chcete přeložit do Morseovy abecedy: ")
        prelozit_do(text_to_encrypt)
        textenc = prelozit_do(text_to_encrypt)
        print("\n Text přeložený do Morseovy abecedy je:", textenc)
    else:
        text_to_decrypt = input("Zadejte text, který chcete preložit z Morseovy abecedy: ")
        prelozit_z(text_to_decrypt)
        textdec = prelozit_z(text_to_decrypt)
        print("\nText přeložený z Morseovy abecedy je:", textdec)
        
