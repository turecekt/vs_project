"""Dragoncurve. This code is used for printing dragon curve in 2 ways in
   L-system and in system of iterated functions"""

import turtle


def functioncycle(iteration):
    r = 'r'  # make variables for the right and left containg 'r' and 'l'
    l = 'l'
    old = r  # assign first iteration a right so we can build off of it
    new = old
    cycle = 1
    while cycle < iteration:
        # keep on generating the next iteration until desired iteration is reached
        new = old + r  # add a right to the end of the old iteration and save it to the new
        old = old[::-1]     # flip the old iteration around
        #  cycling through each character in the flipped old iteration:
        for char in range(0, len(old)):

            if old[char] == r: # if the character is a right:

               old = old[:char] + l + old[char+1:]  # change it to a left

            elif old[char] == l:  # otherwise, if it's a left:

               old = old[:char] + r + old[char+1:]    # change it to a right
        new = new + old  # add the modified old to the new iteration

        old = new  # save the new iteration to old as well for use next cycle
        cycle = cycle+1  # advance cycle variable to keep track of the number of times it's been done
    return new

def functionprinttantsrlrl(printans, new):
    """print rl form of dragon curve"""
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
    backgroundcolor = str(input('Zadajte farbu pozadia:'))  # and background color
    printans = input('Display r/l form?(y/n):')
    if iteration == 0:
        iteration = 9
        length = 10
        pencolor = 'red'
        backgroundcolor = 'black'

    new = functioncycle(iteration)
    print(functionprinttantsrlrl(printans, new))

    # prepare to display the graphics

    turtle.ht()  # do not show the turtle icon when drawing
    turtle.speed(22)  # set drawing speed to fastest(no animation)
    turtle.pencolor(pencolor)  # set pen color as requested
    turtle.bgcolor(backgroundcolor)  # set background color as requested

    turtle.forward(length)  # display segment of desired length to build off of
# cycling through all the characters in the iteration
    for char in range(0, len(new)):

        if new[char] == r: # if the character is a right:

           turtle.right(90)  # turn right at a right angle

           turtle.forward(length)  # go forward desired length

        elif new[char] == l:  # otherwise, if the character is a left:

           turtle.left(90)  # turn left at a right angle

           turtle.forward(length)  # go forward desired length

    turtle.done()