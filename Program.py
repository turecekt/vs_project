"""Hlavni modul aplikace.

Modul obsahujici vstup do cele aplikace.
Umoznuje uzivateli snadne ovladani poskytovanych funkci.
"""


import Enums
import Translator
import sys


def showError(err):
    """Metoda vypisuje naformatovanou chybovou zpravu do konzole.

    Args:
        - err - String obsahujici chybovou zpravu.
    """
    print('\n\t>>>> !!! ' + err + ' !!! <<<<\n')


def showStart():
    """Metoda vypisuje do konzole start aplikace."""
    print('\t***************************************************************')
    print('\t     *****************************************************')
    print('\t          *******************************************\n')
    print('\t                        Dobry den!')
    print('\t                    Vita Vas aplikace')
    print('\n\t                     MORSEOVKA v.1.0\n')
    print('\t     Pomuze Vam s kodovanim/dekodovanim Morseovi abecedy.')
    print('\n\t                   Autor: Filip SPACEK\n')
    print('\t          *******************************************')
    print('\t     *****************************************************')
    print('\t***************************************************************')
    print('\n')


def showEnd():
    """Metoda vypisuje do konzole ukonceni aplikace."""
    print('')
    print('\t***************************************************************')
    print('\t                   Dekuji za spolupraci.')
    print('\t                      Mejte hezky den.')


def showMenu():
    """Metoda vypisuje naformatovane menu do konzole."""
    print('\tMENU')
    print('\t***************************************************************')
    print('\tZ - Zakodovat text do Morseovi abecedy')
    print('\tD - Dekodovat text z Morseovi abecedy')
    print('\tK - Konec')


def parseAction():
    """Metoda vyhodnocuje uzivatelsky vstup a prevadi jej na pozadovanou akci.

    Pokud uzivatel zada chybne vstup, metoda ho upozorni a necha zadat znovu.

    Return:
        - Vrati pozadovanou akci formou vyctoveho typu.
    """
    action = Enums.Actions.UNKNOWN
    while (action == Enums.Actions.UNKNOWN):
        c = input('\tZvolena akce: ').upper()        
        if (c == 'Z'):
            action = Enums.Actions.ENCODE
        elif (c == 'D'):
            action = Enums.Actions.DECODE
        elif (c == 'K'):
            action = Enums.Actions.END
        else:
            showError('Chybne zvolena akce. Zvolte prosim akci dle menu.')
    return action


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


def runProccess(action):
    """Metoda spusti kodovani/dekodovani a vysledek vypise do konzole.

    Args:
        - action - Akce dle vyctoveho typu.
    """
    print('\n\tPREVOD')
    print('\t***************************************************************')
    if (action == Enums.Actions.ENCODE):
        txt = input('\tVepiste text k zakodovani ohraniceny uvozovkami' +
                    ' a bez diakritiky.\n\t')        
        if (not checkUserInputText(txt)):
            showError('Neni zadan text, nebo neni ohranicen uvozovkami.')
        else:
            txt = txt[1:len(txt) - 1]
            translator = Translator.Translator()
            print('\n\t' + translator.encode(txt) + '\n')
    else:
        txt = input('\tVepiste text k dekodovani ohraniceny uvozovkami.' +
                    ' Kazdy znak musi byt oddelen od predchoziho mezerou.' +
                    ' Provolene znaky jsou pouze "." a "-".\n\t')        
        if (not checkUserInputText(txt)):
            showError('Neni zadan text, nebo neni ohranicen uvozovkami.')
        else:
            txt = txt[1:len(txt) - 1]
            translator = Translator.Translator()
            print('\n\t' + translator.decode(txt) + '\n')


# vypiseme do konzole start aplikace
showStart()

# vytvorime behove promenne
appLoop = True
state = Enums.States.MENU
action = Enums.Actions.UNKNOWN

# vytvorime smycku aplikace
while(appLoop):
    if (state == Enums.States.MENU):
        showMenu()
        state = Enums.States.ACTION
    elif (state == Enums.States.ACTION):
        action = parseAction()
        state = Enums.States.PROCCESS
    elif (state == Enums.States.PROCCESS):
        if (action == Enums.Actions.END):
            appLoop = False
        else:
            runProccess(action)
            state = Enums.States.MENU

# vypiseme do konzole konec aplikace
showEnd()
