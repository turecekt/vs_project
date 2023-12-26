import sys
from turtle import *
from enum import Enum


class Colors(Enum):
    blue = 1
    red = 2
    green = 3
    yellow = 4
    black = 5


def koch(a, order, instr=None):
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

def drawSnowflake(iteration, line, background ):
    pencolor(getColor(line))
    bgcolor(getColor(background))
    size = 400

    # Ensure snowflake is center
    penup()
    backward(size / 1.732)
    left(30)
    pendown()

    # Make it fast
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

    # Make the last parts appear
    update()

    exitonclick()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        iteration = int(sys.argv[1])

        print("Choose line color:")
        print("1. Blue")
        print("2. Red")
        print("3. Green")
        print("4. Yellow")
        print("5. Black")
        print("6. White")
        line = int(input("Enter your choice: "))

        print("Choose background color:")
        print("1. Blue")
        print("2. Red")
        print("3. Green")
        print("4. Yellow")
        print("5. Black")
        print("6. White")
        background = int(input("Enter your choice: "))
    else:
        iteration = 4
        line = 6
        background = 1

    drawSnowflake(iteration, line, background)
