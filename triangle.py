import math

def checkIfconstructable(arr):
    """Check if is trinagle constructable.

    Args:
        arr (list): list of coordinants

    Returns:
        bool: True if constructable

    """
    if arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
        return False
    else:
        return True

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