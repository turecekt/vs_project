"""Module (file) docstring."""
import turtle  # Importing the turtle module to use graphics.


def turn_line(a):
    """Drawing Dragon curve."""
    for j in range(len(a)):
        if a[j] == 'r':
            turtle.right(90)
            turtle.forward(10)
        if a[j] == 'l':
            turtle.left(90)
            turtle.forward(10)


def input_data():
    """Input bg and pen cl."""
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


def sides(itr_):
    """Miscalculation of turns."""
    old = 'r'
    new = old

    for i in range(1, itr_, 1):
        new = old + 'r'
        old = old[::-1]
        for j in range(0, len(old)):
            if old[j] == 'r':
                old = old[:j] + 'l' + old[j + 1:]
            else:
                old = (old[:j]) + 'r' + (old[j + 1:])
        new += old
        old = new
    return new


if __name__ == '__main__':
    w = input_data()
    itr = input('Enter the number of iterations:')
    if itr == '':
        itr = 9
    itr = int(itr)
    q = sides(itr)
    turtle.ht()
    turtle.speed(0)
    turn_line(q)
    turtle.done()
