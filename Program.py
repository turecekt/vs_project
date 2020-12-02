"""Hlavni modul aplikace.

Modul obsahujici vstup do cele aplikace.
Umoznuje uzivateli snadne ovladani poskytovanych funkci.
"""


import Enums
import Translator


def formateError(err):
    """Metoda formatuje chybovou zpravu.

    Args:
        - err - String obsahujici chybovou zpravu.
    Return:
        - Naformatovany string chybove zpravy.

    >>> formateError('test')
    '!!! test !!!'
    """
    return '!!! ' + err + ' !!!'


def parseAction(char):
    """Metoda prevadi predany znak na pozadovanou akci.

    Args:
        - char - Znak reprezentujici pozadovanou akci.
    Return:
        - Vrati pozadovanou akci formou vyctoveho typu.

    >>> parseAction('Z')
    1
    """
    c = char.upper()
    if (c == 'Z'):
        return Enums.Actions.ENCODE
    elif (c == 'D'):
        return Enums.Actions.DECODE
    elif (c == 'K'):
        return Enums.Actions.END
    else:
        return Enums.Actions.UNKNOWN


def checkUserInputText(txt):
    """Metoda proveri uzivatelsky vstup, zda-li je spravne zadan.

    Args:
        - txt - String pro otestovani.

    Return:
        - Vrati True, pokud je v poradku, v opacnem pripade vrati False.

    >>> checkUserInputText('"test"')
    True
    """
    return (txt.startswith('"') and txt.endswith('"') and len(txt) > 2)


def encodeText(txt):
    """Metoda zakoduje text do Morseovi abecedy.

    Args:
        - txt - String k zakodovani.
    Return:
        - Zakodovany string.

    >>> encodeText('test')
    '- . ... -'
    """
    return Translator.encode(txt)


def decodeText(txt):
    """Metoda dekoduje text z Morseovi abecedy.

    Args:
        - txt - String k dekodovani.
    Return:
        - Dekodovany string.

    >>> decodeText('- . ... -')
    'TEST'
    """
    return Translator.decode(txt)


# vypiseme do konzole start aplikace
print('***************************************************************')
print('     *****************************************************')
print('          *******************************************')
print('                        Dobry den!')
print('                    Vita Vas aplikace')
print('                     MORSEOVKA v.1.0\n')
print('     Pomuze Vam s kodovanim/dekodovanim Morseovi abecedy.')
print('                   Autor: Filip SPACEK\n')
print('          *******************************************')
print('     *****************************************************')
print('***************************************************************')
print('')

# vytvorime behove promenne
appLoop = False
state = Enums.States.MENU
action = Enums.Actions.UNKNOWN

# vytvorime smycku aplikace
while(appLoop):
    if (state == Enums.States.MENU):
        # menu
        print('MENU')
        print('*****************************************************' +
              '**********')
        print('Z - Zakodovat text do Morseovi abecedy')
        print('D - Dekodovat text z Morseovi abecedy')
        print('K - Konec')
        state = Enums.States.ACTION
    elif (state == Enums.States.ACTION):
        # akce zadana uzivatelem
        action = Enums.Actions.UNKNOWN
        while (action == Enums.Actions.UNKNOWN):
            c = input('Zvolena akce: ')
            action = parseAction(c)
            if (action == Enums.Actions.UNKNOWN):
                print(formateError('Chybne zvolena akce. Zvolte prosim akci' +
                                   ' dle menu.'))
        state = Enums.States.PROCCESS
    elif (state == Enums.States.PROCCESS):
        if (action == Enums.Actions.END):
            appLoop = False
        else:
            print('PREVOD')
            print('**************************************************' +
                  '*************')
            if (action == Enums.Actions.ENCODE):
                txt = input('Vepiste text k zakodovani ohraniceny uvozovkami' +
                            ' a bez diakritiky.\n')
                if (not checkUserInputText(txt)):
                    print(formateError('Neni zadan text, nebo neni ' +
                                       'ohranicen uvozovkami.'))
                else:
                    print(encodeText(txt[1:len(txt) - 1]))
            else:
                txt = input('Vepiste text k dekodovani ohraniceny ' +
                            'uvozovkami. Kazdy znak musi byt oddelen od ' +
                            'predchoziho  mezerou. Provolene znaky jsou ' +
                            'pouze "." a "-".\n')
                if (not checkUserInputText(txt)):
                    print(formateError('Neni zadan text, nebo neni ' +
                                       'ohranicen uvozovkami.'))
                else:
                    print(decodeText(txt[1:len(txt) - 1]))
            state = Enums.States.MENU

# vypiseme do konzole konec aplikace
print('')
print('***************************************************************')
print('                   Dekuji za spolupraci.')
print('                      Mejte hezky den.')
