"""Include files."""
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


new = ''
left = 'l'
right = 'r'
number = 0
linecolor = 'r'  # b, g, r, c, m, y, k, w
backgroundcolor = 'k'

position = 0
size = 0
angle_right = 0
angle_left = (3 - angle_right)


"""
 Move left
 in = pos , count , angle
 returns modified positions x, y
 1 = up , 0 = no change , -1 = down
 [90,180,270,360] degree
 [1,0,-1,0] = y
 [0,-1,0,1] = x
"""


def move_left(posx, posy, cnt, angle):
    """
    Move left function.

    >>> move_left([0], [0], 0, 0)
    (0, 1)
    """
    # saves input values to local
    local_posx = posx
    local_posy = posy
    # defines a table for x and y coordinates rotation
    static_y = [1, 0, -1, 0]  # static mapping
    static_x = [0, -1, 0, 1]  # static mapping
    # load to x and y
    # merge x and y value with static table
    # replace new value to old one
    x = local_posx[cnt]
    x = x + static_x[angle]
    local_posx[cnt] = x

    y = local_posy[cnt]
    y = y + static_y[angle]
    local_posy[cnt] = y
    # Return modified value
    return local_posx[cnt], local_posy[cnt]


"""
 Move right
 in = pos , count , angle
 returns modified positions x, y
 1 = up , 0 = no change , -1 = down
 [90,180,270,360] degree
 [-1,0,1,0] = y
 [0,-1,0,1] = x
"""


def move_right(posx, posy, cnt, angle):
    """
    Move right function.

    >>> move_right([0], [0], 0, 0)
    (0, -1)
    """
    # saves input values to local
    local_posx = posx
    local_posy = posy
    # defines a table for x and y coordinates rotation
    static_y = [-1, 0, 1, 0]  # static mapping
    static_x = [0, -1, 0, 1]  # static mapping
    # load to x and y
    # merge x and y value with static table
    # replace new value to old one
    x = local_posx[cnt]
    x = x + static_x[angle]
    local_posx[cnt] = x
    y = local_posy[cnt]
    y = y + static_y[angle]
    local_posy[cnt] = y
    # Return modified value
    return local_posx[cnt], local_posy[cnt]


def generate_dragon(iteration):
    """
    Generate Heighway Dragon line route.

    returns generated line route.
    >>> generate_dragon(1)
    ('r', 'l', 'r')
    """
    old = right
    new = old
    loop_cycle = 1
    while loop_cycle < iteration:
        new = (old) + (right)
        old = old[::-1]
        for char in range(0, len(old)):
            if old[char] == right:
                old = (old[:char]) + (left) + (old[char+1:])
            elif old[char] == left:
                old = (old[:char]) + (right) + (old[char+1:])
        new = (new) + (old)
        old = new
        loop_cycle = loop_cycle+1
    return new


def update():
    """
    Graph update function.

    No return.
    """
    global dragon, x, y, position, size, angle_left, angle_right
    if(position < size-1):
        if new[position] == (right):  # right
            if(new[position-1] == (right)):
                angle_right += 1
                if(angle_left < 0):
                    angle_left = 0
                if(angle_right > 3):
                    angle_right = 0
            else:
                angle_right = 3 - angle_left
                if(angle_right < 0):
                    angle_right = 0
                if(angle_right > 3):
                    angle_right = 0

            x[position], y[position] = move_right(x, y, position, angle_right)
        elif new[position] == (left):  # left
            if(new[position-1] == (left)):
                angle_left += 1
                if(angle_left > 3):
                    angle_left = 0
            else:
                angle_left = 3-(angle_right)
                if(angle_left < 0):
                    angle_left = 0
            x[position], y[position] = move_left(x, y, position, angle_left)
        else:  # done or empty
            pass
        dragon.setData(x, y)
        position += 1
        x[position] = x[position-1]  # store old pos to new
        y[position] = y[position-1]  # store old pos to new
    return 0


def main(arg):
    """Do main function that Reads input and displays dragon."""
    global new, left, right, app, backgroundcolor, dragon
    global size, x, y, win, timer, linecolor, number
    if(len(arg) == 1):
        number = 9
    if(len(arg) == 2):  # count of iteration
        number = int(arg[1])
    elif(len(arg) == 3):  # color of draw line
        number = int(arg[1])
        linecolor = str(arg[2])
    elif(len(arg) == 4):  # color of background
        number = int(arg[1])
        linecolor = str(arg[2])
        backgroundcolor = str(arg[3])

    new = generate_dragon(number)
    size = len(new)

    app = QtGui.QApplication([])
    x = np.zeros(size)
    y = np.zeros(size)

    win = pg.GraphicsLayoutWidget(show=True, title="Dragon")
    win.setBackground(backgroundcolor)
    win.resize(1024, 768)

    plot = win.addPlot(title="Dragon plot")

    dragon = plot.plot(x, y, pen=linecolor)
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1)
    return 0


if __name__ == '__main__':
    import sys
    stop = main(sys.argv)
    if(stop == 1):
        sys.exit()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
