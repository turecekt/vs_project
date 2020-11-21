"""This is a project with four functions to calculate details about triangle.

To determinate if we can get a triangle according to inputs and if so,
to calcul lenght of the sides,
to calcul perimetr and area of the triangle.

Unit tests:
>>> checkNumbers("1,2,3,4,5,6")
True

>>> checkNumbers("1,x,3,y,5,6")
False

>>> checkLenght("1,2,3,4,5,6")
True

>>> checkLenght("1,2,3,4")
False
"""


def checkNumbers(coords):
    """Check if all inputs are a numbers.

    Args:
        - coords - Input of the function

    Returns:
        - true or false - Output of the function
    """
    numbers = map(str, coords.split(","))

    for x in numbers:
        if not x.isnumeric():
            return False

    return True


def checkLenght(coords):
    """Check if input includes exactly six numbers.

    Args:
        - coords - Input of the function

    Returns:
        - true or false - Output of the function
    """
    if len(coords.split(",")) != 6:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Triangle summary")
    areNumbers = False

    while not areNumbers:
        coords = input("Enter numbers x1,y1,x2,y2,x3,y3 seperated by coma:")

        if not checkNumbers(coords):
            print("All six enters have to be the numbers")
            areNumbers = False
        else:
            areNumbers = True

        if not checkLenght(coords):
            print("Please enter exactly six numbers")
            areNumbers = False
        else:
            areNumbers = True
