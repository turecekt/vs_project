from decimal import Decimal

class Vector2:
    xCoordinate = 0
    yCoordinate = 0

    def __init__(self, xCoordinate, yCoordinate):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def __str__(self):
        return f"[{self.xCoordinate}, {self.yCoordinate}]"


def isConstructable():
    """
    Find is triangle can be constructed.

    Return boolean informing about constructablity of a triangle
    >>> isConstructable(???)
    ???
    """
    return False


def getSideLenght(pointA, pointB):
    """
    Find length of a side.

    Return side length
    >>> getSideLenght(???)
    ???
    """
    return 1


def getPerimeter(sideA, sideB, sideC):
    """
    Find perimeter of a triangle.

    Return triangle perimeter
    >>> getPerimeter(???)
    ???
    """
    return 1


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
    area = (s*(s-sideA)*(s-sideB)*(s-sideC)) ** 0.5

    return area


def isRightAngled():
    """
    Find if triangle is rightangled.

    Return true if triangle is right angled
    >>> isRightAngled(???)
    ???
    """
    return False


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

    if pointA is None and pointB is None and pointC is None:
        print("You will be now asked to input coordinates of your triangle")
        print()
        print("Please, input each point of triangle like this => [5;6]")
        print("You can use decimal numbers like this => [5.1;6.5]")
        print("Other input will be rejected!")
        print()

        # getting user input
        print("Now enter your triangle coordinates:")
        pointARawData = input('Enter first point: ')
        pointBRawData = input('Enter second point: ')
        pointCRawData = input('Enter third point: ')

        # converting raw data in string form into vector form
        pointA = convertRawPointDataIntoVector(pointARawData)
        pointB = convertRawPointDataIntoVector(pointBRawData)
        pointC = convertRawPointDataIntoVector(pointCRawData)

    # calculating side lenghts based of end points coordinates
    sideA = getSideLenght(pointA, pointB)
    sideB = getSideLenght(pointB, pointC)
    sideC = getSideLenght(pointC, pointA)

    # displaying result information
    print()
    print("==============================================================")
    print("====================TRIANGLE INFORMATION======================")
    print("==============================================================")
    print("Data used for calculations:")
    print("Point A coordinates => " + str(pointA))
    print("Point B coordinates => " + str(pointB))
    print("Point C coordinates => " + str(pointC))
    print("--------------------------------------------------------------")
    print("Triangle sides lengths:")
    print("Side A lenght => " + str(sideA))
    print("Side A lenght => " + str(sideB))
    print("Side A lenght => " + str(sideC))
    print()


# Executes the main function
if __name__ == '__main__':
    main()
