#!/usr/bin/env python3
"""Processes input for triangle program."""

import sys
import math


def sideLength(point1, point2):
    """Return lenghts of sides."""
    return math.sqrt(
                     math.pow((int(point2[0]) - int(point1[0])), 2)
                     + math.pow((int(point2[1]) - int(point1[1])), 2)
                    )


def getSides():
    args = sys.argv
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
    return [length1, length2, length3]