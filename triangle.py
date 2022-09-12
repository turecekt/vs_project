"""Triangle program core definitions"""
import math

def start(args):
    """Demonstrate an example to start with."""
    if len(args) != 7:
        print('Please provide 6 numbers \
                in format point1x point1y point2x point2y point3x point3y')
    else:
        point1 = (args[1], args[2])
        point2 = (args[3], args[4])
        point3 = (args[5], args[6])

        #Points
        print(f"Points are {point1} {point2} {point3}")

        #Side length
        length1 = sideLength(point1, point2)
        length2 = sideLength(point2, point3)
        length3 = sideLength(point3, point1)

        print(f"Lengths of the sides of the triangle are: {length1}, {length2}, {length3}")

        #Perimeter
        perimeter = trianglePerimeter(length1, length2, length3)

        print(f"Perimeter of the triangle is: {perimeter}")

def sideLength(point1, point2):
    return math.sqrt(math.pow((int(point2[0]) - int(point1[0])), 2) + math.pow((int(point2[1]) - int(point1[1])), 2))

def trianglePerimeter(a, b, c):
    return a + b + c

def triangleArea():
    pass
