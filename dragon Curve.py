import turtle
r = 'r' #make variables for the right and left containg 'r' and 'l'
l = 'l'
old = r #assign our first iteration a right so we can build off of it
new = old
iteration = 9
length = 6
pencolor = 'red'
backgroundcolor = 'black'
iteration = int(input('Zadajte pocet iterácii:'))   #input the user's desired iteration, segment length, pen color
length = int(input('Zadajte dĺžku každého segmentu:'))
pencolor = str(input('Zadajte farbu pera:'))
backgroundcolor = str(input('Zadajte farbu pozadia:')) #and background color
if iteration == 0:
    iteration = 9
    length = 10
    pencolor = 'red'
    backgroundcolor = 'black'

r = 'r' #make variables for the right and left containg 'r' and 'l'
l = 'l'
old = r #assign our first iteration a right so we can build off of it
new = old
iteration = 9
length = 6

cycle = 1
def functioncycle():

 while cycle < iteration:    #keep on generating the next iteration until desired iteration is reached
    new = old + r  #add a right to the end of the old iteration and save it to the new
    old = old[::-1]     #flip the old iteration around(as in the the first charicter becomes last)
#cycling through each character in the flipped old iteration:
    for char in range(0, len(old)):
        #if the character is a right:
        if old[char] == r:
            #change it to a left
            old = old[:char] + l + old[char+1:]
        #otherwise, if it's a left:
        elif old[char] == l:

           old = old[:char] + r + old[char+1:]    #change it to a right
    new = new + old  #add the modified old to the new iteration
    #save the new iteration to old as well for use next cycle
    old = new #save the new iteration to old as well for use next cycle
    cycle = cycle+1 #advance cycle variable to keep track of the number of times it's been done
printans=input('Display r/l form?(y/n):')
def functionprinttantsrlrl():
    if printans == 'y':
     print(new)

 # set background color as requested
#prepare to display the graphics
turtle = turtle.Turtle()
turtle.ht() #do not show the turtle icon when drawing
turtle.speed(22) #set drawing speed to fastest(no animation)
turtle.pencolor(pencolor) #set pen color as requested
#set background color as requested
turtle.screen.bgcolor(backgroundcolor)
#display segment of desired length to build off of
turtle.forward(length)
#cycling through all the characters in the iteration
for char in range(0, len(new)):
    #if the character is a right:
    if new[char] == r:
        #turn right at a right angle
        turtle.right(90)
        #go forward desired length
        turtle.forward(length)
    #otherwise, if the character is a left:
    elif new[char] == l:
        #turn left at a right angle
        turtle.left(90)
        #go forward desired length
        turtle.forward(length)

