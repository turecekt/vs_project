#!/usr/bin/env python3
"""Input processing functions for triangle program."""

import math
from decimal import Decimal


def sideLength(point1, point2):
    """Distance between point1 and point2 with coordinates x (index 0) and y (index 1)

    :return: Lenght of side.
    """
    return round(Decimal(math.dist(point1, point2)), 10)
#    vector = (point2[0] - point1[0], point2[1] - point1[1])
#    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def inputPoint(point, coordNames=["x", "y"], debug=False):
    """Ask user to input coordinates of one point.
    Function suuport multi-dimension space based on cordNames provided.
    User is asked to import point coordinates one by one and checks,
    if inputed coordinate is valid number. If not, it lets user to input
    coordinate again up to 3 times. Then, if input is not coorect, program
    is exited with exit code 1.

    :return: List of coordinates entered to console.
    """
    coords = []
    for coordName in coordNames:
        nok = True
        retries = 0
        while nok:
            try:
                print(f"Please input point {point}, "
                      f"coordinate {coordName}: ", end="")
                coords.append(float(input()))
                nok = False
            except Exception as e:
                print(e) if debug else None
                if retries < 2:
                    print("Wrong input! Try again...")
                    retries += 1
                else:
                    print("Retry limit exceeded, exiting...")
                    exit(1)
    return coords


def getPoints(args, debug=False):
    """Coordinates are parsed from provided command line arguments list (args)
    or interactively inputed to console by user.

    :return: List of 3 points with 2 coordinates each.
    """
    try:
        points = [
            [float(args[1]), float(args[2])],
            [float(args[3]), float(args[4])],
            [float(args[5]), float(args[6])],
        ]
    except (ValueError, IndexError) as e:
        print("Failed to process provided arguments or no arguments given.")
        print(f"Reason: {e}") if debug else None
        print("Please enter points now.")
        points = [
            inputPoint("A", debug=debug),
            inputPoint("B", debug=debug),
            inputPoint("C", debug=debug),
        ]
    return points


def getSides(args, debug=False):
    """:return: List of lengths of the 3 sides of a triangle."""
    points = getPoints(args, debug)

    # Points
    print(f"\nDebug: Points are {points[0]} {points[1]}"
          f"{points[2]}\n") if debug else None

    # Side length
    sides = []
    sides.append(sideLength(points[0], points[1]))
    sides.append(sideLength(points[1], points[2]))
    sides.append(sideLength(points[2], points[0]))

    return sides
