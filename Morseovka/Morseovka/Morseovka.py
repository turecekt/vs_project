def TextToMorse(text):
    sp = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
          'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
          'o': '---', 'p':
              '.--.', 'q': '--.-',
          'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
          'y': '-.--', 'z': '--..',
          '.': '.', '-': '-', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
          '5': '.....',
          '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '}
    mozne = set('abcdefghijklmnopqrstyuvwx.1234567890 ') # vsechny mozne symboly, ktere se mohou zapsat do promenne
    stroka = ''
    for i in text: # kontrola zadaneho textu
        if set(i).difference(mozne): # kontroluje, jestli symbol ze zadaneho textu se lisi od moznych symbolu
            print('nespravne znaky')
            stroka = 'nespravne znaky'
            break
        for j in i: # vypisuje prelozeny text
                print(sp[j], end=" ")
                stroka = stroka + ' ' + sp[j] # zapisuje prelozeny text do promenne
        print()
    if stroka == '': # kontroluje, jestli do stroki je zapsana jenom mezera
          print('prazdne pole')
          return('prazdne pole')
    else:
         return(stroka)
