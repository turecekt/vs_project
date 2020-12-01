def isConstructable():
    """
    Find is triangle can be constructed.

    Return boolean informing about constructablity of a triangle
    >>> isConstructable(???)
    ???
    """ 

def getSideLenght(pointA, pointB):
    """
    Find length of a side.

    Return side length
    >>> getSideLenght(???)
    ???
    """ 

def getPerimeter(sideA, sideB, sideC):
    """
    Find perimeter of a triangle.

    Return triangle perimeter
    >>> getPerimeter(???)
    ???
    """ 

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
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    return area

def isRightAngled():
    """
    Find if triangle is rightangled.

    Return true if triangle is right angled
    >>> isRightAngled(???)
    ???
    """ 

def main():
    # getting user input
    pointA = float(input('Enter first point: '))
    pointB = float(input('Enter second point: '))
    pointC = float(input('Enter third point: '))


# Executes the main function
if __name__ == '__main__':
    main()