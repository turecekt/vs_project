import sys
from turtle import *
from enum import Enum


class Colors(Enum):
    blue = 1
    red = 2
    green = 3
    yellow = 4
    black = 5


def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, order - 1)
            left(t)
    else:
        forward(a)

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


    # Choose colours and size
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
    for i in range(3):
        koch(size, iteration)
        right(120)

    end_fill()

    # Make the last parts appear
    update()

    exitonclick()
