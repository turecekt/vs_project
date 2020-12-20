import morse


def test_skuska1():
    """ Overenie toho, ze prekladac dokaze prelozit individualne znaky. """
    assert morse.prekladac('A') == '.- '

    """ Overenie toho, ze prekladac dokaze prelozit cele slova. """
    assert morse.prekladac('SKUSKA2') == '... -.- ..- ... -.- .- ..--- '

    """ Overenie toho, ze prekladac dokaze prelozit medzery v texte. """
    assert morse.prekladac('M E D Z E R E') \
           == '-- | . | -.. | --.. | . | .-. | . '

    """ Overenie toho, ze prekladac dokaze prelozit symboly v texte. """
    assert morse.prekladac(',?YM80LY/') \
           == '--..-- ..--.. -.-- -- ---.. ----- .-.. -.-- -..-. '

    """ Overenie toho, ze prekladac dokaze prelozit cele vety pisane
    pomocou malych pismen) """
    assert morse.prekladac('male na velke') \
           == '-- .- .-.. . | -. .- | ...- . .-.. -.- . '
