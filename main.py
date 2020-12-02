from decimal import Decimal
import math
from math import isclose


class Vector2:
    """
    A class to represent a 2D plane position in form of a Vector 2D.

    Attributes
    ----------
    xCoordinate : str
        x coordinate position in plane
    yCoordinate : str
        y coordinate position in plane

    Methods
    -------
    __init__(xCoordinate, yCoordinate):
        Constructs new instance of the class

    __str__()
        Overrides default str() behaviour
    """

    xCoordinate = 0
    yCoordinate = 0

    def __init__(self, xCoordinate, yCoordinate):
        """
        Vector2 constructor.

        Args:
            xCoordinate ([Decimal]): X coordinate as decimal
            yCoordinate ([Decimal]): Y coordinate as decimal
        """
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def __str__(self):
        """
        Override str() for Vector2 class.

        Returns:
            [string]: "vector2 class in formatted string form"
        """
        return f"[{self.xCoordinate}; {self.yCoordinate}]"


def isConstructable(sideA, sideB, sideC):
    """
    Find is triangle can be constructed.

    Args:
        sideA ([type]): [description]
        sideB ([type]): [description]
        sideC ([type]): [description]

    Returns:
        [bool]: Return boolean informing about constructablity of a triangle
    """
    return (
        sideA + sideB >= sideC
        and sideB + sideC > sideA
        and sideC + sideA > sideB
    )


def getSideLenght(pointA, pointB):
    """
    Find length of a side.

    Return side length
    >>> getSideLenght(???)
    ???
    """
    return (Decimal)(
        math.sqrt(math.pow(pointB.xCoordinate - pointA.xCoordinate, 2)
                  + math.pow(pointB.yCoordinate - pointA.yCoordinate, 2))
    )


def getPerimeter(sideA, sideB, sideC):
    """
    Find perimeter of a triangle.

    Return triangle perimeter
    >>> getPerimeter(???)
    ???
    """
    return sideA + sideB + sideC


def getArea(sideA, sideB, sideC):
    """
    Find area of a triangle.

    Return size of an area of a triangle
    >>> getArea(???)
    ???
    """
    # calculate the semi-perimeter
    s = (sideA + sideB + sideC) / 2

    # calculate the area
    # √(s*(s-a)*(s-b)*(s-c))
    area = math.sqrt(s * (s-sideA) * (s-sideB) * (s-sideC))

    return area


def isRightAngled(sideA, sideB, sideC):
    """
    Find if triangle is rightangled.

    Return true if triangle is right angled
    >>> isRightAngled(???)
    ???
    """
    sideAPow = math.pow(sideA, 2)
    sideBPow = math.pow(sideB, 2)
    sideCPow = math.pow(sideC, 2)
    return (
        (isclose(sideAPow + sideBPow, sideCPow, abs_tol=0.0001))
        or (isclose(sideCPow + sideBPow, sideAPow, abs_tol=0.0001))
        or (isclose(sideAPow + sideCPow, sideBPow, abs_tol=0.0001))
    )


def isRawPointDataStringValid(rawData):
    """
    Check if raw point data is valid.

    Return validity boolean
    >>> convertRawPointDataIntoVector("[5;5]")
    return True
    """
    if rawData.count('[') != 1 or not rawData.startswith('['):
        return False
    if rawData.count(']') != 1 or not rawData.endswith(']'):
        return False
    if rawData.count(';') != 1:
        return False
    return True


def convertRawPointDataIntoVector(rawData):
    """
    Convert raw point data into it's vector coordinates form.

    Return converted raw data in vector form
    >>> convertRawPointDataIntoVector("[5;5]")
    return Vector2(5, 5)
    """
    if not isRawPointDataStringValid(rawData):
        return None
    else:
        firstCoordinate = 0
        secondCoordinate = 0
        isNextCoordinateNegative = False
        tempNumberString = ""
        for character in rawData:
            if character == '[' or character == ' ':
                continue
            if character == '-':
                isNextCoordinateNegative = True
                continue
            if character == ';':
                firstCoordinate = Decimal(tempNumberString)
                if isNextCoordinateNegative:
                    firstCoordinate = firstCoordinate * -1

                tempNumberString = ""
                isNextCoordinateNegative = False
                continue
            if character == ']':
                secondCoordinate = Decimal(tempNumberString)
                if isNextCoordinateNegative:
                    secondCoordinate = secondCoordinate * -1
                continue
            if (
                character == '0' or character == '1'
                or character == '2' or character == '3'
                or character == '4' or character == '5'
                or character == '6' or character == '7'
                or character == '8' or character == '9'
                or character == '.'
               ):
                tempNumberString += character
                continue
            else:
                return None

        return Vector2(firstCoordinate, secondCoordinate)


def main():
    """Execute main logic flow of the program."""
    # defining star variables
    pointA = None
    pointB = None
    pointC = None

    # uncomment these 3 lines below to skip CLI input and use parameter values
    """
    pointA = Vector2(0, 0)
    pointB = Vector2(5, 0)
    pointC = Vector2(0, 5)
    """

    # inform user about program functionality
    print()
    print("===============================================")
    print("Welcome to the ultimate triangle analysis tool!")
    print("===============================================")
    print()
    print("This program gives you basic information about your triangle.")

    exitProgramTriggered = False
    while not exitProgramTriggered:
        if pointA is None and pointB is None and pointC is None:
            print()
            print("===================================================")
            print("You will be now asked to input triangle coordinates")
            print()
            print("Please, input each point of triangle like this => [5;6]")
            print("You can use decimal numbers like this => [5.1;6.5]")
            print("Other input will be rejected!")
            print()

            # getting user input
            # and converting raw data in string form into vector form
            print("Now enter your triangle coordinates:")
            while pointA is None:
                pointARawData = input('Enter first point: ')
                pointA = convertRawPointDataIntoVector(pointARawData)
                if pointA is None:
                    print("Invalid input!")
                    print()

            while pointB is None:
                pointBRawData = input('Enter second point: ')
                pointB = convertRawPointDataIntoVector(pointBRawData)
                if pointB is None:
                    print("Invalid input!")
                    print()

            while pointC is None:
                pointCRawData = input('Enter third point: ')
                pointC = convertRawPointDataIntoVector(pointCRawData)
                if pointC is None:
                    print("Invalid input!")
                    print()

        # calculating side lenghts based of end points coordinates
        sideA = getSideLenght(pointB, pointC)
        sideB = getSideLenght(pointC, pointA)
        sideC = getSideLenght(pointA, pointB)

        # calculating triangle constructability
        canBeConstructed = isConstructable(sideA, sideB, sideC)

        # calculating triangle perimeter
        trianglePerimeter = getPerimeter(sideA, sideB, sideC)

        # calculating triangle area
        triangleArea = getArea(sideA, sideB, sideC)

        # calculating if trianble is
        isTriangleRightAngled = isRightAngled(sideA, sideB, sideC)

        # displaying result information
        print()
        print("============================================================")
        print("====================TRIANGLE INFORMATION====================")
        print("============================================================")
        print("Data used for calculations:")
        print("Point A coordinates => " + str(pointA))
        print("Point B coordinates => " + str(pointB))
        print("Point C coordinates => " + str(pointC))
        print("----------------------------------------------------------")
        print("Is triangle constructable? => " + str(canBeConstructed))
        print("----------------------------------------------------------")
        if canBeConstructed:
            print("Triangle sides lengths:")
            print("Side A lenght => " + str(round(sideA, 5)))
            print("Side B lenght => " + str(round(sideB, 5)))
            print("Side C lenght => " + str(round(sideC, 5)))
            print("----------------------------------------------------------")
            print("Triangle perimeter: => " + str(round(trianglePerimeter, 5)))
            print("----------------------------------------------------------")
            print("Triangle area: => " + str(round(triangleArea, 5)))
            print("----------------------------------------------------------")
            print("Is triangle right angled? => " + str(isTriangleRightAngled))
            print("----------------------------------------------------------")
            print()
        else:
            print()
            print("No other info, triangle is non constructable!")

        # setting variables to default end logic loop value
        exitProgramTriggered = True
        pointA = None
        pointB = None
        pointC = None

        # prints out instruction for end user input
        print("Send 'r' to calculate new triangle")
        print("Send any other key to exit program or press 'Enter'")

        # handles user input at end of a logic loop
        logicEndUserInput = input("Your input: ")
        if logicEndUserInput == 'r' or logicEndUserInput == 'R':
            exitProgramTriggered = False


# Executes the main function
if __name__ == '__main__':
    main()
