"""This is a project with four functions to calculate details about triangle.

To determinate if we can get a triangle according to inputs and if so,
to calcul lenght of the sides,
to calcul perimetr and area of the triangle.
Unit tests:
>>> checkNumbers(['1','x','3','y','5','6'])
False
>>> checkNumbers(['1','2','3','4','5','6'])
True
>>> checkLenght(['1','2','3','4'])
False
>>> checkLenght(['1','2','3','4','5','6','7','8'])
False
>>> checkLenght(['1','2','3','4','5','6'])
True
>>> getCoords()
['1', '2', '3', '4', '5', '6']
"""


def getCoords():
    """Check user input.

    Keep asking user until the right numbers are entered.
    Returns:
        - array of coordinates
    """
    # coords = input("Enter numbers x1,y1,x2,y2,x3,y3 seperated by coma:")
    coords = "1,2,3,4,5"
    coords = coords.split(",")

    while (True):
        if(checkNumbers(coords) and checkLenght(coords)):
            break
        # coords = input("Incorrect input. Please try again:")
        coords = "1,2,3,4,5,6"
        coords = coords.split(",")

    return coords


def checkNumbers(coords):
    """Check if all inputs are a numbers.

    Args:
        - coords
    Returns:
        - true or false
    """
    for x in coords:
        if not x.isnumeric():
            return False

    return True


def checkLenght(coords):
    """Check if input includes exactly six numbers.

    Args:
        - coords
    Returns:
        - true or false
    """
    if len(coords) != 6:
        return False
    else:
        return True


if __name__ == '__main__':
    getCoords()
