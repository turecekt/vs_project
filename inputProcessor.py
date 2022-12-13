#!/usr/bin/env python3
"""Processes input for triangle program."""


def sideLength(point1, point2):
    """Returns lenght of side."""
    vector = (point2[0] - point1[0], point2[1] - point1[1])
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def inputPoint(point, coordNames=["x", "y"], debug=False):
    coords = []
    for coordName in coordNames:
        nok = True
        retries = 0
        while nok:
            try:
                print(f"Please input point {point}, coordinate {coordName}: ", end="")
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
            inputPoint("A"),
            inputPoint("B"),
            inputPoint("C"),
        ]
    return points


def getSides(args, debug=False):

    points = getPoints(args, debug)

    # Points
    print(f"\nDebug: Points are {points[0]} {points[1]} {points[2]}\n") if debug else None

    # Side length
    sides = []
    sides.append(sideLength(points[0], points[1]))
    sides.append(sideLength(points[1], points[2]))
    sides.append(sideLength(points[2], points[0]))
  
    return sides
