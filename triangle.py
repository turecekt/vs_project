"""This is triangle module.

Triangle module supplies many useful functions for trinagle computation
in two dimensional space such as lengthOfSide() etc.

>>> checkIfconstructable([[1,1],[1,2],[2,3]])
True
>>> checkIfconstructable([[1,1],[1,2],[1,3]])
False
>>> lengthOfSide([1,1],[1,12])
11.0
>>> countArea([3,5,4])
6.0
>>> checkIfRightAngled([3,5,4])
True
>>> countPerimeter([1,2,3,4])
10
"""

import math


def checkIfconstructable(arr):
    """Check if is trinagle constructable.

    Args:
        arr (list): list of points

    Returns:
        bool: True if constructable

    """
    a = lengthOfSide(arr[0], arr[1])
    b = lengthOfSide(arr[1], arr[2])
    c = lengthOfSide(arr[2], arr[0])
    return a + b > c and a + c > b and b + c > a


def lengthOfSide(A, B):
    """Count distance between two points in two dimensiaonal space.

    Args:
        A (list): point coordinants
        B (list): point coordinants

    Returns:
        float: distance between two points

    """
    return math.sqrt((B[0] - A[0])*(B[0] - A[0])+(B[1]-A[1])*(B[1]-A[1]))


def countPerimeter(distances):
    """Count perimeter from distances.

    Args:
        distances (list): list of distances

    Returns:
        int: sum of all distances


    """
    return sum(distances)


def countArea(distances):
    """Count area of triangle using Heron's formula.

    Args:
        distances (list): list of distances

    Returns:
        float: area

    """
    s = sum(distances)/2
    return math.sqrt(s*(s - distances[0]) *
                     (s - distances[1])*(s - distances[2]))


def checkIfRightAngled(distances):
    """Check if triangle is right angeled using Pythagorean Theorem Formula.

    Args:
        distances (list): list of distances

    Returns:
        bool: True if right angeled

    """
    sortedDistances = list(distances)
    sortedDistances.sort()
    if (sortedDistances[2]*sortedDistances[2] == sortedDistances[1] *
       sortedDistances[1] + sortedDistances[0]*sortedDistances[0]):
        return True
    else:
        return False
