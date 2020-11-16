from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


new = ''
left = ''
right = ''
number = 0
linecolor = 'k'

position = 0
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
    """Move left function."""
    local_posx = posx
    local_posy = posy
    static_y = [1, 0, -1, 0]
    static_x = [0, -1, 0, 1]
    x = local_posx[cnt]
    x = x + static_x[angle]
    local_posx[cnt] = x
    y = local_posy[cnt]
    y = y + static_y[angle]
    local_posy[cnt] = y
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
    """Move right function."""
    local_posx = posx
    local_posy = posy
    static_y = [-1, 0, 1, 0]  # static mapping
    static_x = [0, -1, 0, 1]  # static mapping
    x = local_posx[cnt]
    x = x + static_x[angle]
    local_posx[cnt] = x
    y = local_posy[cnt]
    y = y + static_y[angle]
    local_posy[cnt] = y
    return local_posx[cnt], local_posy[cnt]


def generate_dragon(iteration):
    """
     Generate Heighway Dragon line route.
     returns generated line route
    """
    right = 'r'
    left = 'l'
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
    return new, left, right


def update():
    """Graph update function.
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


def main():
    global new, left, right, app, backgroundcolor, dragon
    global size, x, y, win, timer

    """Input values."""
    number = int(input('Pocet interakci:'))
    linecolor = 'k'  # input('Barva cary:')
    backgroundcolor = 'k'  # input('Barva pozadi:')

    new, left, right = generate_dragon(number)
    size = len(new)

    app = QtGui.QApplication([])
    x = np.zeros(size)
    y = np.zeros(size)

    win = pg.GraphicsLayoutWidget(show=True, title="Dragon")
    win.setBackground(linecolor[0])
    win.resize(1024, 768)

    plot = win.addPlot(title="Dragon plot")

    dragon = plot.plot(x, y)
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1)


if __name__ == '__main__':
    import sys
    main()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
