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

 angle (0-3)
 1 = up , 0 = no change , -1 = down
 [90,180,270,360] degree
 [1,0,-1,0] = y
 [0,-1,0,1] = x
"""


def move_left(posx, posy, cnt, angle):
    """
    Move left function.

    Args:
        - posx - array of x positions
        - posy - array of y positions
        - cnt  - position in array
        - angle - angle of rotation [0-3]
    Returns:
        - posx[cnt] - modified value of x position
        - posy[cnt] - modified value of y position

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
    tmp_x = local_posx[cnt]
    tmp_x = tmp_x + static_x[angle]
    local_posx[cnt] = tmp_x

    tmp_y = local_posy[cnt]
    tmp_y = tmp_y + static_y[angle]
    local_posy[cnt] = tmp_y
    # Return modified value
    return local_posx[cnt], local_posy[cnt]


"""
 Move right
 in = pos , count , angle
 returns modified positions x, y

 angle (0-3)
 1 = up , 0 = no change , -1 = down
 [90,180,270,360] degree
 [-1,0,1,0] = y
 [0,-1,0,1] = x
"""


def move_right(posx, posy, cnt, angle):
    """
    Move right function.

    Args:
        - posx - array of x positions
        - posy - array of y positions
        - cnt  - position in array
        - angle - angle of rotation [0-3]
    Returns:
        - posx[cnt] - modified value of x position
        - posy[cnt] - modified value of y position

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
    tmp_x = local_posx[cnt]
    tmp_x = tmp_x + static_x[angle]
    local_posx[cnt] = tmp_x
    tmp_y = local_posy[cnt]
    tmp_y = tmp_y + static_y[angle]
    local_posy[cnt] = tmp_y
    # Return modified value
    return local_posx[cnt], local_posy[cnt]


def generate_dragon(iteration):
    """
    Generate Heighway Dragon line route.

    Args:
        - iteration - number of iterations

    Returns:
        - new - array of generated line routing

    >>> generate_dragon(1)
    'r'
    """
    old = right
    new = old
    loop_cycle = 1
    while loop_cycle < iteration:  # loop until number of iteration is met
        new = (old) + (right)  # add right to new and store it to new
        old = old[::-1]  # reverse old
        for char in range(0, len(old)):  # for each character in old
            if old[char] == right:  # if it is right
                old = (old[:char]) + (left) + (old[char+1:])  # move it left
            elif old[char] == left:  # if it is left
                old = (old[:char]) + (right) + (old[char+1:])  # move it right
        new = (new) + (old)  # add it to new
        old = new  # replace old with new
        loop_cycle = loop_cycle+1  # increase cycle
    return new


def modify_pos(local_x, local_y,
               pos, local_angle_left,
               local_angle_right, local_size,
               local_new):
    """Modify generated line route function.

    Function modifies plot position array with predefined plot direction
    Args:   x array,
            y array,
            current position in array
            angle change left,
            angle change right,
            size of arrays,
            array of generated line route

    Returns: modified x array,
            modified y array,
            current position
            modified angle left
            modified angle right
            unchanged line route array

    angle_left is reversed value of angle_right
    angle_right [0,1,2,3]
    angle_left  [3,2,1,0]

    >>> modify_pos([0,0,0,0], [0,0,0,0], 1, -1, -4, 3, ['r','l'])
    ([0, 1, 1, 0], [0, 0, 0, 0], 2, 3, 0, ['r', 'l'])
    """
    if(pos < local_size-1):
        if local_new[pos] == (right):  # right
            if(local_new[pos-1] == (right)):  # if previous was same
                local_angle_right += 1  # increase angle
                if(local_angle_left < 0):  # Limit value
                    local_angle_left = 0
                if(local_angle_right > 3):
                    local_angle_right = 0
            else:  # if previous was diffrent
                # calculate reversed value
                local_angle_right = 3 - local_angle_left
                if(local_angle_right < 0):  # Limit value
                    local_angle_right = 0
                if(local_angle_right > 3):
                    local_angle_right = 0
                if(local_angle_left < 0):
                    local_angle_left = 0
                if(local_angle_left > 3):
                    local_angle_left = 3
            # get modified position
            local_x[pos], local_y[pos] = move_right(local_x, local_y, pos,
                                                    local_angle_right)
        elif local_new[pos] == (left):  # left
            if(local_new[pos-1] == (left)):  # if previous was same
                local_angle_left += 1  # increase angle
                if(local_angle_left > 3):  # Limit value
                    local_angle_left = 0
            else:  # if previous was diffrent
                # calculate reversed value
                local_angle_left = 3-(local_angle_right)
                if(local_angle_left < 0):  # Limit value
                    local_angle_left = 0
                if(local_angle_left > 3):
                    local_angle_left = 3
                if(local_angle_right < 0):
                    local_angle_right = 0
                if(local_angle_right > 3):
                    local_angle_right = 0
            # get modified position
            local_x[pos], local_y[pos] = move_left(local_x, local_y, pos,
                                                   local_angle_left)
        pos += 1  # increase position
        local_x[pos] = local_x[pos-1]  # store old pos to new
        local_y[pos] = local_y[pos-1]  # store old pos to new
    return local_x, local_y, pos, local_angle_left, \
        local_angle_right, local_new


def update():
    """
    Graph update function.

    No return value.
    """
    global dragon, x, y, position, angle_left, angle_right, size, new
    x, y, position, angle_left, angle_right, new = modify_pos(x, y, position,
                                                              angle_left,
                                                              angle_right,
                                                              size, new)
    dragon.setData(x, y)  # update plot


def arg_decode(argument):
    """CLI input decode function.

    Args:
        - argument - array of console arguments
    Returns:
        - iter_number - number of iterations
        - line_color - color of line
        - background_color - color of background
        - -1 - if no argument

    Decodes console input values.
    Returns numer of iterations, color of line and background.
    """
    if(len(argument) == 1):  # if no values received
        iter_number = 9
        return iter_number, 'r', 'k'  # set iteration to 9
    if(len(argument) == 2):  # count of iteration
        iter_number = int(argument[1])
        return iter_number, 'r', 'k'
    elif(len(argument) == 3):  # color of draw line
        iter_number = int(argument[1])
        loc_linecolor = str(argument[2])
        return iter_number, loc_linecolor, 'k'
    elif(len(argument) == 4):  # color of background
        iter_number = int(argument[1])
        loc_linecolor = str(argument[2])
        loc_backgroundcolor = str(argument[3])
        return iter_number, loc_linecolor, loc_backgroundcolor
    return -1


def main(arg):
    """Do main function that Reads input and displays dragon.

    Args:
        - arg- arguments passed from console
    """
    global new, left, right, app, backgroundcolor, dragon
    global size, x, y, win, timer, linecolor, number
    number, linecolor, backgroundcolor = arg_decode(arg)
    new = generate_dragon(number)  # Generate dragon plot values

    app = QtGui.QApplication([])  # create plot application
    size = (len(new)+1)  # get size of new
    x = np.zeros(size)  # create array of zeros based on size of new
    y = np.zeros(size)

    # set plot application settings
    win = pg.GraphicsLayoutWidget(show=True, title="Dragon")
    win.setBackground(backgroundcolor)
    win.resize(1024, 768)

    plot = win.addPlot(title="Dragon plot")  # add plot

    static_posx = [-1, 0, 0]  # predefined cords for lines
    static_posy = [0, 0, -1]  #
    dragon = plot.plot(static_posx, static_posy, pen=linecolor)
    dragon = plot.plot(x, y, pen=linecolor)  # plot empty arrays
    timer = QtCore.QTimer()  # Init timer
    timer.timeout.connect(update)  # join timer update to funtion
    timer.start(1)  # set timer update time


if __name__ == '__main__':
    import sys
    main(sys.argv)
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
