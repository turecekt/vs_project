class Vector2:
    xCoordinate = 0
    yCoordinate = 0

    def __init__(self, xCoordinate, yCoordinate):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

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

def convertRawPointDataIntoVector(rawData):
    """
    Convert raw point data into it's vector coordinates form

    Return converted raw data in vector form
    >>> convertRawPointDataIntoVector(???)
    ???
    """ 

    pointCoordinates = Vector2(0,0)
    return pointCoordinates

def main():
    # inform user about program functionality
    print()
    print("Welcome to the ultimate triangle analysis tool!")
    print()
    print("This program gives you basic information about your triangle.")
    print("You will be now asked to input coordinates of your triangle")
    print()
    print("Please, input each point of triangle like this => [5;6]")
    print("Other input will be rejected!")
    print()

    # getting user input
    print("Now enter your triangle coordinates:")
    pointARawData = float(input('Enter first point: '))
    pointBRawData = float(input('Enter second point: '))
    pointCRawData = float(input('Enter third point: '))

    # converting raw data in string form into vector form
    pointA = convertRawPointDataIntoVector(pointARawData)
    pointB = convertRawPointDataIntoVector(pointBRawData)
    pointC = convertRawPointDataIntoVector(pointCRawData)

    # calculating side lenghts based of end points coordinates
    sideA = getSideLenght(pointA, pointB)
    sideB = getSideLenght(pointB, pointC)
    sideC = getSideLenght(pointC, pointA)


# Executes the main function
if __name__ == '__main__':
    main()