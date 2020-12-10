def morse_code(var_inp):
    """
    Morse encoder.

    Returns encoded string
    """
    var_inp = var_inp.lower()

    charInp = list(var_inp)

    strLen = len(charInp)

    for y in range(strLen):
        if charInp[y] == 'á':
            charInp[y] = "a"
        elif charInp[y] == 'č':
            charInp[y] = "c"
        elif charInp[y] == 'ď':
            charInp[y] = "d"
        elif charInp[y] == 'ě':
            charInp[y] = "e"
        elif charInp[y] == 'é':
            charInp[y] = "e"
        elif charInp[y] == 'í':
            charInp[y] = "i"
        elif charInp[y] == 'ň':
            charInp[y] = "n"
        elif charInp[y] == 'ó':
            charInp[y] = "o"
        elif charInp[y] == 'ř':
            charInp[y] = "r"
        elif charInp[y] == 'š':
            charInp[y] = "s"
        elif charInp[y] == 'ť':
            charInp[y] = "t"
        elif charInp[y] == 'ú':
            charInp[y] = "u"
        elif charInp[y] == 'ů':
            charInp[y] = "u"
        elif charInp[y] == 'ý':
            charInp[y] = "y"
        elif charInp[y] == 'ž':
            charInp[y] = "z"
        elif charInp[y] == '"':
            charInp[y] = ''

    for x in range(strLen):
        if charInp[x] == 'a':
            charInp[x] = ".- "
        elif charInp[x] == 'b':
            charInp[x] = "-... "
        elif charInp[x] == 'c':
            charInp[x] = "-.-. "
        elif charInp[x] == 'd':
            charInp[x] = "-.. "
        elif charInp[x] == 'e':
            charInp[x] = ". "
        elif charInp[x] == 'f':
            charInp[x] = "..- "
        elif charInp[x] == 'g':
            charInp[x] = "--. "
        elif charInp[x] == 'h':
            charInp[x] = ".... "
        elif charInp[x] == 'i':
            charInp[x] = ".. "
        elif charInp[x] == 'j':
            charInp[x] = ".--- "
        elif charInp[x] == 'k':
            charInp[x] = "-.- "
        elif charInp[x] == 'l':
            charInp[x] = ".-.. "
        elif charInp[x] == 'm':
            charInp[x] = "-- "
        elif charInp[x] == 'n':
            charInp[x] = "-. "
        elif charInp[x] == 'o':
            charInp[x] = "--- "
        elif charInp[x] == 'p':
            charInp[x] = ".--. "
        elif charInp[x] == 'q':
            charInp[x] = "--.- "
        elif charInp[x] == 'r':
            charInp[x] = ".-. "
        elif charInp[x] == 's':
            charInp[x] = "... "
        elif charInp[x] == 't':
            charInp[x] = "- "
        elif charInp[x] == 'u':
            charInp[x] = "..- "
        elif charInp[x] == 'v':
            charInp[x] = "...- "
        elif charInp[x] == 'w':
            charInp[x] = ".-- "
        elif charInp[x] == 'x':
            charInp[x] = "-..- "
        elif charInp[x] == 'y':
            charInp[x] = "-.-- "
        elif charInp[x] == 'z':
            charInp[x] = "--.. "
        elif charInp[x] == ' ':
            charInp[x] = "/ "
        elif charInp[x] == '1':
            charInp[x] = ".---- "
        elif charInp[x] == '2':
            charInp[x] = "..--- "
        elif charInp[x] == '3':
            charInp[x] = "...-- "
        elif charInp[x] == '4':
            charInp[x] = "....- "
        elif charInp[x] == '5':
            charInp[x] = "..... "
        elif charInp[x] == '6':
            charInp[x] = "-.... "
        elif charInp[x] == '7':
            charInp[x] = "--... "
        elif charInp[x] == '8':
            charInp[x] = "---.. "
        elif charInp[x] == '9':
            charInp[x] = "----. "
        elif charInp[x] == '0':
            charInp[x] = "----- "
        elif charInp[x] == '.':
            charInp[x] = ".-.-.- "
        elif charInp[x] == ',':
            charInp[x] = "--..-- "
        elif charInp[x] == ':':
            charInp[x] = "---... "
        elif charInp[x] == '?':
            charInp[x] = "..--.. "
        elif charInp[x] == '-':
            charInp[x] = "-....- "
        elif charInp[x] == '/':
            charInp[x] = "-..-. "
        elif charInp[x] == '@':
            charInp[x] = ".--.-. "
        elif charInp[x] == '=':
            charInp[x] = "-...- "
    strInpMorse = ""
    for tmp in charInp:
        strInpMorse += tmp

    return strInpMorse


def morse_decode(var_inp2):
    """
    Morse decoder.

    Returns decoded string
    """
    cnt = 0
    for spc in var_inp2:
        if spc.isspace():
            cnt = cnt + 1

    for i in range(cnt):
        if '"' in var_inp2:
            var_inp2 = var_inp2.replace('"', ' ')
        elif "-.-- " in var_inp2:
            var_inp2 = var_inp2.replace("-.-- ", 'y')
        elif ".-.-.- " in var_inp2:
            var_inp2 = var_inp2.replace(".-.-.- ", '.')
        elif "--..-- " in var_inp2:
            var_inp2 = var_inp2.replace("--..-- ", ',')
        elif "---... " in var_inp2:
            var_inp2 = var_inp2.replace("---... ", ':')
        elif "..--.. " in var_inp2:
            var_inp2 = var_inp2.replace("..--.. ", '?')
        elif "-....- " in var_inp2:
            var_inp2 = var_inp2.replace("-....- ", '-')
        elif "-..-. " in var_inp2:
            var_inp2 = var_inp2.replace("-..-. ", '/')
        elif ".--.-. " in var_inp2:
            var_inp2 = var_inp2.replace(".--.-. ", '@')
        elif "-...- " in var_inp2:
            var_inp2 = var_inp2.replace("-...- ", '=')
        elif "-... " in var_inp2:
            var_inp2 = var_inp2.replace("-... ", 'b')
        elif "-.-. " in var_inp2:
            var_inp2 = var_inp2.replace("-.-. ", 'c')
        elif ".... " in var_inp2:
            var_inp2 = var_inp2.replace(".... ", 'h')
        elif ".--- " in var_inp2:
            var_inp2 = var_inp2.replace(".--- ", 'j')
        elif ".-.. " in var_inp2:
            var_inp2 = var_inp2.replace(".-.. ", 'l')
        elif ".--. " in var_inp2:
            var_inp2 = var_inp2.replace(".--. ", 'p')
        elif "--.- " in var_inp2:
            var_inp2 = var_inp2.replace("--.- ", 'q')
        elif "...- " in var_inp2:
            var_inp2 = var_inp2.replace("...- ", 'v')
        elif ".-- " in var_inp2:
            var_inp2 = var_inp2.replace(".-- ", 'w')
        elif "-..- " in var_inp2:
            var_inp2 = var_inp2.replace("-..- ", 'x')
        elif "--.. " in var_inp2:
            var_inp2 = var_inp2.replace("--.. ", 'z')
        elif "..- " in var_inp2:
            var_inp2 = var_inp2.replace("..- ", 'u')
        elif "-.. " in var_inp2:
            var_inp2 = var_inp2.replace("-.. ", 'd')
        elif "..- " in var_inp2:
            var_inp2 = var_inp2.replace("..- ", 'f')
        elif "--. " in var_inp2:
            var_inp2 = var_inp2.replace("--. ", 'g')
        elif "-.- " in var_inp2:
            var_inp2 = var_inp2.replace("-.- ", 'k')
        elif "--- " in var_inp2:
            var_inp2 = var_inp2.replace("--- ", 'o')
        elif ".-. " in var_inp2:
            var_inp2 = var_inp2.replace(".-. ", 'r')
        elif "... " in var_inp2:
            var_inp2 = var_inp2.replace("... ", 's')
        elif "-- " in var_inp2:
            var_inp2 = var_inp2.replace("-- ", 'm')
        elif "-. " in var_inp2:
            var_inp2 = var_inp2.replace("-. ", 'n')
        elif ".- " in var_inp2:
            var_inp2 = var_inp2.replace(".- ", 'a')
        elif ".. " in var_inp2:
            var_inp2 = var_inp2.replace(".. ", 'i')
        elif ". " in var_inp2:
            var_inp2 = var_inp2.replace(". ", 'e')
        elif "- " in var_inp2:
            var_inp2 = var_inp2.replace("- ", 't')
        elif "/ " in var_inp2:
            var_inp2 = var_inp2.replace("/ ", ' ')
        elif ".---- " in var_inp2:
            var_inp2 = var_inp2.replace(".---- ", '1')
        elif "..--- " in var_inp2:
            var_inp2 = var_inp2.replace("..--- ", '2')
        elif "...-- " in var_inp2:
            var_inp2 = var_inp2.replace("...-- ", '3')
        elif "....- " in var_inp2:
            var_inp2 = var_inp2.replace("....- ", '4')
        elif "..... " in var_inp2:
            var_inp2 = var_inp2.replace("..... ", '5')
        elif "-.... " in var_inp2:
            var_inp2 = var_inp2.replace("-.... ", '6')
        elif "--... " in var_inp2:
            var_inp2 = var_inp2.replace("--... ", '7')
        elif "---.. " in var_inp2:
            var_inp2 = var_inp2.replace("---.. ", '8')
        elif "----. " in var_inp2:
            var_inp2 = var_inp2.replace("----. ", '9')
        elif "----- " in var_inp2:
            var_inp2 = var_inp2.replace("----- ", '0')
    var_inp2 = var_inp2[1:]  # Remove space before text
    return var_inp2


if __name__ == '__main__':
    print('Morse Encoder/Decoder')
    print('d for decode')
    print('e for encode')
    print('Enter what you want to do: ')
    strChoice = input()
    if strChoice == 'e':
        print('Enter text to encode: ')
        strInp = input()
        strInpOrg = strInp
        var = morse_code(strInp)
        print(var)
    elif strChoice == 'd':
        print('Enter text to decode: ')
        strInp = input()
        strInpOrg = strInp
        var = morse_decode(strInp)
        print(var)
    else:
        print('Wrong choice...')
        print('Exiting...')
