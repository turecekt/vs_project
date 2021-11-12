def morse():
	decision = input("For encoding morse press 1, For decoding morse press 2, for exit press 3:")
	decision = int(decision)
	if (decision == 3):
		print("Konec")
	else:
		if (decision == 1):
            text = input("Enter text to encode:")
			encode(text)
			input("Press Enter to continue")
			morse()
		elif (decision == 2):
            text = input("Enter morse code to decode, write '/' after every letter, write '//' after every word:")
			decode(text)
			input("Press Enter to continue")
			morse()
		else:
			print("Your input isn't 1 or 2")
			input("Press Enter to continue")
			morse()

# Slovnik obsahujici znaky morseovky
morseovka = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Funkce zakoduje do morseovky
def encode(zprava):
    try:
        zprava = zprava.upper()
        kod = ''
        for pismeno in zprava:
            if pismeno != ' ':
 
                # Najde ve slovniku odpovidajici kod pro jednotlive znaky
                kod = kod + morseovka[pismeno] + '/'
            else:
                # 1 / jsou ruzne znaky, 2 / ruzna slova
                kod += '/'
 
        return kod
    # Pøi nedefinovaném vstupu se vypíše chybová hláška
    except KeyError: 
        print("Znak", pismeno, "není definovaný v morseovì abecedì")
        print("Definované znaky jsou: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )")
       