import morse


# Overenie toho, ze prekladac dokaze prelozit individualne znaky.
def test_skuska1():
    assert morse.prekladac('A') == '.- '


# Overenie toho, ze prekladac dokaze prelozit cele slova.
def test_skuska2():
    assert morse.prekladac('SKUSKA2') == '... -.- ..- ... -.- .- ..--- '


# Overenie toho, ze prekladac dokaze prelozit medzery v texte.
def test_skuska3():
    assert morse.prekladac('M E D Z E R E') \
           == '-- | . | -.. | --.. | . | .-. | . '


# Overenie toho, ze prekladac dokaze prelozit symboly v texte.
def test_skuska4():
    assert morse.prekladac(',?YM80LY/') \
           == '--..-- ..--.. -.-- -- ---.. ----- .-.. -.-- -..-. '


# Overenie toho, ze prekladac dokaze prelozit cele vety pisane
# pomocou malych pismen)
def test_skuska5():
    assert morse.prekladac('male na velke') \
           == '-- .- .-.. . | -. .- | ...- . .-.. -.- . '
