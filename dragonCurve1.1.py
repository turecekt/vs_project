"""
DragonCurve1.1.py This code is used for printing dragon curve in 2 ways
in L-system and in system of iterated functions.
"""

import turtle


def functioncycle(iteration):
      """Function that is used for printing iterations"""
    
    r = 'r'  # make variables for the right and left containg 'r' and 'l'
    l = 'l'
    old = r  # assign first iteration a right so we can build off of it
    new = old
    cycle = 1
    while cycle < iteration:
        # keep on generating next iteration until desired iteration is reached
        new = old + r  # add a right to the end of the old iteration
        old = old[::-1]     # flip the old iteration around
        #  cycling through each character in the flipped old iteration:
        for char in range(0, len(old)):

            if old[char] == r:
                # if the character is a right:

               old = old[:char] + l + old[char+1:]  # change it to a left

            elif old[char] == l:  # otherwise, if it's a left:

               old = old[:char] + r + old[char+1:]    # change it to a right
        new = new + old  # add the modified old to the new iteration

        old = new  # save the new iteration to old as well for use next cycle
        cycle = cycle+1
    return new


def functionprinttantsrlrl(printans, new):
    
    """Print rl form of dragon curve"""
    if printans == 'y':
        return new
    else:
        return ""


if __name__ == '__main__':
    r = 'r'  # make variables for the right and left containg 'r' and 'l'
    l = 'l'

    iteration = int(input('Zadajte pocet iterácii:'))  # input of pen color
    length = int(input('Zadajte dĺžku každého segmentu:'))
    pencolor = str(input('Zadajte farbu pera:'))
    backgroundcolor = str(input('Zadajte farbu pozadia:'))  # and bg color
    printans = input('Display r/l form?(y/n):')
    if iteration == 0:
        iteration = 9
        length = 10
        pencolor = 'red'
        backgroundcolor = 'black'

    new = functioncycle(iteration)
    print(functionprinttantsrlrl(printans, new))

    turtle.ht()  # do not show the turtle icon when drawing
    turtle.speed(22)  # set drawing speed to fastest(no animation)
    turtle.pencolor(pencolor)  # set pen color as requested
    turtle.bgcolor(backgroundcolor)  # set background color as requested

    turtle.forward(length)
    # display segment of desired length to build off of

    for char in range(0, len(new)):

        if new[char] == r:  # if the character is a right:

            turtle.right(90)  # turn right at a right angle

            turtle.forward(length)  # go forward desired length

        elif new[char] == l:  # otherwise, if the character is a left:

            turtle.left(90)  # turn left at a right angle

            turtle.forward(length)  # go forward desired length

    turtle.done()
