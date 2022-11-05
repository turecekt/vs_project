"""Triangle program core definitions."""
import math


def start(args):
    """Print results of default calculations."""
    if len(args) != 7:
        print('Please provide 6 numbers '
              'in format point1x point1y point2x point2y point3x point3y')
    else:
        point1 = (args[1], args[2])
        point2 = (args[3], args[4])
        point3 = (args[5], args[6])

        # Points
        print(f"Points are {point1} {point2} {point3}")

        # Side length
        length1 = sideLength(point1, point2)
        length2 = sideLength(point2, point3)
        length3 = sideLength(point3, point1)

        print("Lengths of the sides of the triangle are:\n"
              f"{length1}, {length2}, {length3}")

        # Perimeter
        perimeter = trianglePerimeter(length1, length2, length3)

        print(f"Perimeter of the triangle is: {perimeter}")

        # Area
        area = triangleArea(length1, length2, length3)

        print(f"Area of the triangle is: {area}")

        # Orthogonality
        sides = [lenght1, length2, length3]
        hyponetuse = max(sides)
        orthogonal = orthogonality()




def sideLength(point1, point2):
    """Return lenghts of sides."""
    return math.sqrt(
                     math.pow((int(point2[0]) - int(point1[0])), 2)
                     + math.pow((int(point2[1]) - int(point1[1])), 2)
                    )


def trianglePerimeter(a, b, c):
    """Return perimeter."""
    return a + b + c


def triangleArea(a, b, c):
    """Return triangle area."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def constructability(a, b, c):
    """Return constructability"""
    return (a + b > c) and (b + c > a) and (c + a > b)

def triangleOrthogonality(leg1, leg2, hypotenuse):
    """Return orthogonality"""
    return math.pow(hypotenuse, 2) == math.pow(leg1, 2) + math.pow(leg2, 2)
