"""Test module for number extraction methods."""


import number_extractions


stringCli = "1,2,3,4,-10,-11,22,0,16,-4"


#   ExtractNumbersFromCLI
def test_ExtractNumbersFromCLI__stringGiven__typeReturnedIsList():
    """Assert that given parameter is parsed correctly.

    It will be returned as list of integers.
    """
    v = number_extractions.ExtractNumbersFromCLI(stringCli)
    assert isinstance(v, list)


def test_ExtractNumbersFromCLI__stringGiven__listItemsAreEqual():
    """Count is equal to count in string comma separated values.

    It will compare integer count on either side.
    """
    v = number_extractions.ExtractNumbersFromCLI(stringCli)
    assert v == [1, 2, 3, 4, -10, -11, 22, 0, 16, -4]


def test_ExtractNumbersFromCLI__corruptStringGiven__raisesValueError():
    """Corrupt string is given.

    Raises ValueError exception.
    """
    try:
        number_extractions.ExtractNumbersFromCLI("1,3,'3',-4")
    except ValueError as exc:
        assert True, f"Exception raised as expected {exc}"


#   ExtractNumbersFromFile
def test_ExtractNumbersFromFile__stringGiven__typeReturnedIsList():
    """Loads vector from file.

    Type returned is list.
    """
    v = number_extractions. \
        ExtractNumbersFromFile('./minimax/modules/test_vector.txt')
    assert isinstance(v, list)


def test_ExtractNumbersFromFile__stringGiven__listItemsAreEqual():
    """Loads vector from file.

    Vector is equal to a given sequence.
    """
    v = number_extractions. \
        ExtractNumbersFromFile('./minimax/modules/test_vector.txt')
    assert v == [1, 2, 3, 4, -10, -11, 22, 0, 16, -4]


def test_ExtractNumbersFromFile__corruptStringGiven__raisesValueError():
    """While loading vector from test_vector_corrupt raises error.

    On of the element is not easily parsable to integer.
    """
    try:
        number_extractions. \
            ExtractNumbersFromFile('./minimax/modules/test_vector_corrupt.txt')
    except ValueError:
        assert True
    else:
        assert False


#   GenerateRandomVectorLength20
def test_GenerateRandomVectorLength20__X__typeReturnedIsList():
    """Generates a random numeric vector of length 20.

    Type returned is list.
    """
    v = number_extractions.GenerateRandomVectorLength20()
    assert isinstance(v, list)


def test_GenerateRandomVectorLength20__X__listContains20Elements():
    """Generates a random numeric vector of length 20.

    The length is 20.
    """
    v = number_extractions.GenerateRandomVectorLength20()
    assert len(v) == 20


def test_GenerateRandomVectorLength20__X__listContainsIntegersOnly():
    """Generates a random numberic vector of length 20.

    Every single item of the list is of type integer.
    """
    v = number_extractions.GenerateRandomVectorLength20()
    t = True
    for item in v:
        if type(item) is not int:
            t = not t
    assert t
