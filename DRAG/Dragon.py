import turtle
import time

""" turn_line - # function for drawing Dragon curve"""


def turn_line(a):
    for j in range(len(a)):
        if a[j] == 'r':
            turtle.right(90)
            turtle.forward(10)
        if a[j] == 'l':
            turtle.left(90)
            turtle.forward(10)


"""input_data - function to enter background and pen colors"""


def input_data():
    data = []
    for i in range(2):
        if i == 0:
            data.append(input('Enter background color:'))
        if i == 1:
            data.append(input('Enter pen color:'))
    if data[0] == '':
        data[0] = 'red'
    turtle.color(data[0])
    if data[1] == "":
        data[1] = 'black'
    turtle.bgcolor(data[1])
    return data


"""sides - function for calculating rotations Dragon curve"""


def sides(itr):
    old = 'r'
    new = old
    turtle.ht()
    turtle.speed(0)
    turtle.forward(10)
    for i in range(1, itr, 1):
        new = old + 'r'
        old = old[::-1]
        for i in range(0, len(old)):
            if old[i] == 'r':
                old = old[:i] + 'l' + old[i + 1:]
            else:
                old = (old[:i]) + 'r' + (old[i + 1:])
        new += old
        old = new
    return new


w = input_data()
itr = input('Enter the number of iterations:')
if itr == '':
    itr = 9
itr = int(itr)
q = sides(itr)
turn_line(q)
time.sleep(20)
