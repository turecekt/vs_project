#!/usr/bin/env python3
"""Run triangle program."""

from math import hypot
import sys
from triangle import *


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
        sides = [length1, length2, length3]
        otherSides = []
        for side in sides:
            if side != max(sides):
                otherSides.append(side)
            else:
                hypotenuse = side
        orthogonal = triangleOrthogonality(otherSides[0], otherSides[1], hypotenuse)


start(sys.argv)