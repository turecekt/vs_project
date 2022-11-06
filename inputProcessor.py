#!/usr/bin/env python3
"""Processes input for triangle program."""

import sys


def sideLength(point1, point2):
    """Return lenghts of sides."""
    vector = (point2[0] - point1[0], point2[1] - point1[1])
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def getSides():
    args = sys.argv
    if len(args) != 7:
        print('Please provide 6 numbers '
              'in format point1x point1y point2x point2y point3x point3y')
    else:
        point1 = (float(args[1]), float(args[2]))
        point2 = (float(args[3]), float(args[4]))
        point3 = (float(args[5]), float(args[6]))

        # Points
        print(f"Points are {point1} {point2} {point3}")

        # Side length
        length1 = sideLength(point1, point2)
        length2 = sideLength(point2, point3)
        length3 = sideLength(point3, point1)

        print("Lengths of the sides of the triangle are:\n"
              f"{length1}, {length2}, {length3}")
    return [length1, length2, length3]
