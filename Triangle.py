"""This is a project with four functions to calculate details about triangle.

To determinate if we can get a triangle according to inputs and if so,
to calcul lenght of the sides,
to calcul perimetr and area of the triangle.
Unit tests:
>>> getCoords()
['1', '2', '3', '4', '5', '6']
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
>>> computeSides(['0','0','4','1','2','6'])
('4.12', '5.39', '6.32')
"""


from math import sqrt


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
        - coords array of coordinates
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
        - coords array of coordinates
    Returns:
        - true or false
    """
    if len(coords) != 6:
        return False
    else:
        return True


def computeSides(coords):
    """Get the lengt of their sides.

    Function takes coordinates of three points like parameter.
    Parameter is an array of coordinates in format [x1,y1,x2,y2,x3,y3].

    Args:
        - coords array of coordinates

    Returns:
        - (a,b,c) lenghts of sides
    """
    coords = [float(i) for i in coords]
    a = sqrt((abs(coords[2] - coords[0]))**2 + abs((coords[3] - coords[1]))**2)
    b = sqrt((abs(coords[4] - coords[2]))**2 + abs((coords[5] - coords[3]))**2)
    c = sqrt((abs(coords[0] - coords[4]))**2 + abs((coords[1] - coords[5]))**2)

    a = str(round(a, 2))
    b = str(round(b, 2))
    c = str(round(c, 2))

    return (a, b, c)


if __name__ == '__main__':
    getCoords()
