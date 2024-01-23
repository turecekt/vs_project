import sys
from turtle import *
from enum import Enum



def koch(a, order, instr=None):
    """ Function contains algorithm that draws one side of Koch's snowflake

    Args:
        a (int): Size
        order (int): Number of Koch's snowflake iteration 
        instr (List[Tuple[str, int]]): List of turtle instruction

    Returns:
        List[Tuple[str, int]]: _description_
    """
    if instr is None:
        instr = []

    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, order - 1, instr)
            left(t)
            instr.append(('left', t))
    else:
        forward(a)
        instr.append(('forward', a))

    return instr


def getColor(num):
    """ Function contains case returning color string 

    Args:
        num (int): Number assigned to a specific color

    Returns:
        string: Name of color 
    """
    match num:
        case 1:
            return "blue"
        case 2:
            return "red"
        case 3:
            return "green"
        case 4:
            return "yellow"
        case 5:
            return "black"
        case 6:
            return "white"


def drawSnowflake(iteration, line, background):
    """ Function sets up snowflake parameters, starting position and puts together all 3 sides of Koch's snowflake

    Args:
        iteration (int): Number of Koch's snowflake iteration 
        line (string): Color of snowflake 
        background (string): Color of background
    """
    
    pencolor(getColor(line))
    bgcolor(getColor(background))
    fillcolor('white')
    width(2)
    size = 400

    # Centers snowflake
    penup()
    backward(size / 1.732)
    left(30)
    pendown()

    # Makes turtle run faster
    tracer(100)
    hideturtle()
    speed(0)
    begin_fill()

    # Three Koch curves
    instruction = []
    for i in range(3):
        koch(size, iteration)
        right(120)

    end_fill()

    update()

    exitonclick()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        iteration = int(sys.argv[1])
        if iteration > 9:
            iteration = 9
        if iteration < 0:
            iteration = 0

        print("Choose line color:")
        print("Blue = 1")
        print("Red = 2")
        print("Green = 3")
        print("Yellow = 4")
        print("Black = 5")
        print("White = 6")
        line = int(input("Enter your choice: "))

        print("Choose background color:")
        print("Blue = 1")
        print("Red = 2")
        print("Green = 3")
        print("Yellow = 4")
        print("Black = 5")
        print("White = 6")
        background = int(input("Enter your choice: "))
    else:
        # Defalut configuration
        iteration = 4
        line = 6
        background = 1

    drawSnowflake(iteration, line, background)
