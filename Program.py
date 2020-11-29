import Enums
import Translator

def showError(err):
    print('\n\t>>>> !!! ' + err + ' !!! <<<<\n')

def showMenu():
    print('\tMENU')
    print('\t***************************************************************')
    print('\tZ - Zakodovat text do Morseovi abecedy')
    print('\tD - Dekodovat text z Morseovi abecedy')
    print('\tK - Konec')

def parseAction():
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
    return (txt.startswith('"') and txt.endswith('"') and len(txt) > 2)

def runProccess(action):
    print('\n\tPREVOD')
    print('\t***************************************************************')                
    if (action == Enums.Actions.ENCODE):        
        txt = input('\tVepiste text k zakodovani ohraniceny uvozovkami.\n\t')
        if (not checkUserInputText(txt)):
            showError('Neni zadan text, nebo neni ohranicen uvozovkami.')
        txt = txt[1:len(txt) - 1]
        translator = Translator.Translator()
        print('\n\t' + translator.encode(txt) + '\n')
    else:
        txt = input('\tVepiste text k dekodovani ohraniceny uvozovkami. Kazdy znak musi byt oddelen od predchoziho mezerou.\n\t')
        if (not checkUserInputText(txt)):
            showError('Neni zadan text, nebo neni ohranicen uvozovkami.')
        txt = txt[1:len(txt) - 1]
        translator = Translator.Translator()
        print('\n\t' + translator.decode(txt) + '\n')
        

            
            
    
    
            

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
print('\t***************************************************************\n\n')




appLoop = True
state = Enums.States.MENU
action = Enums.Actions.UNKNOWN


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
        
    


print('\n\t***************************************************************')
print('\t                   Dekuji za spolupraci.')
print('\t                      Mejte hezky den.')


