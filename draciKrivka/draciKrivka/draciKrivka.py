
# import the turtle module to use turtle graphics
import turtle
  
iterace = int(input('Zadejte pocet iteraci: '))

barvaPera = input('Zadejte barvu pera: ')

barvaPozadi = input('Zadejte barvu pozdi: ')

def Krivka(iterace, delka, uhel):
     if iterace == 0:
        turtle.forward(delka)
     else:
         Krivka(iterace - 1, delka, 90)
         turtle.left(uhel)
         Krivka(iterace - 1, delka, -90)
     
       

turtle.Screen().clear()
turtle.speed(0 )
turtle.pensize(2)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

if barvaPera:
    turtle.color(barvaPera)
else:
    turtle.color('red')

if barvaPozadi:
    turtle.bgcolor(barvaPozadi)
else:
    turtle.bgcolor('black')
    


delka = 5
uhel = 90


Krivka(iterace, delka, uhel)

turtle.done()