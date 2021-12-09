
# import the turtle module to use turtle graphics
import turtle
  


def Krivka(n, delka, uhel):
     if n == 0:
        turtle.forward(delka)
     else:
         Krivka(n - 1, delka, 90)
         turtle.left(uhel)
         Krivka(n - 1, delka, -90)
       



turtle.Screen().clear()
turtle.speed(0 )
turtle.pensize(2)
#turtle.color(barvaPozadi)
#turtle.bgcolor(barvaPozadi)

barvaPera = input('Zadejte barvu pera: ') 

def barvaPera():
    if barvaPera == '':
        turtle.color('red')
    else:
        turtle.color(barvaPera)

barvaPozadi = input('Zadejte barvu pozadi: ')

def barvaPozadi():
    if barvaPozadi == '':
        turtle.bgcolor('black')
    else:
        turtle.bgcolor(barvaPera)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

n = 30
delka = 5
uhel = 90


Krivka(n, delka, uhel)

turtle.done()