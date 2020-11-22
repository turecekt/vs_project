"""This is input reading module.

Input reading module suplies functions for reading values from stdin
and parse them to coordinantes.

>>> parsePoint('(11,1)')
[11.0, 1.0]
>>> parsePoint('5.2,7.6')
[5.2, 7.6]
>>> getPoints(['1','2','3'], "test")
[[1.0, 1.0], [1.0, 2.0], [1.0, 3.0]]
"""


def parsePoint(pointInput):
    """Parse point to coordinates pair (list of two numbers).

    Args:
        pointInput (string): pointInput read from terminal

    Returns:
        list: x and y coordinates (pair)

    Raises:
        Exception: when coordinantes are in invalid format or are not numbers

    """
    unifiedPointInput = pointInput
    removeChars = ["(", ")", " ", "[", "]"]
    for char in removeChars:
        unifiedPointInput.replace(char, "")
    coordinantes = unifiedPointInput.split(",")
    if (len(coordinantes) < 2 or len(coordinantes) > 2):
        raise Exception("Wrong format of point. Allowed formats ar 'number, number' and '(number, number)'")
    return[float(coordinantes[0]), float(coordinantes[1])]


def getPoints(pointsNames, enviroment):
    """Read point from terminal.

    Args:
        pointsNames (list of strings): name of the points in two dimensional space
        enviroment (string): enviroment of app

    Returns:
        list: list of points

    Raises:
        Exception: Wrong format of point.

    """
    points = []
    for pointName in pointsNames:
        question = "Please enter coordinante (x,y) of point "+pointName+": "
        if enviroment == "__main__":
            point = input(question)
        else:
            point = "1,"+point+""
        points.append(parsePoint((point)))
    return points
