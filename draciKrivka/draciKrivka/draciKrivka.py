
"""Heighway Dragon."""

# Naimportovani turtle modulu pro pouziti grafiky a _tkinter pro vymezeni vyjimek u funkci
import turtle
import _tkinter


# definovani promennych z inputu uzivatele
print('Seznam dostupnych barev: blue, green, red, cyan, megenta, yellow, white, black')

# vyzve uzivatele pro zadani poctu iteraci
#iterace = input('Zadejte pocet iteraci: ')
def parametry():
    global iterace
    global barvaPera
    global barvaPozadi
    global delka
    global uhel
    iterace = input('Zadejte pocet iteraci: ')
    barvaPera = input('Zadejte barvu pera: ')
    barvaPozadi = input('Zadejte barvu pozadi: ')
    delka = 2
    uhel = 90

# vyzve uzivatele pro zadani barvy pera
#barvaPera = input('Zadejte barvu pera: ')

# vyzve uzivatele pro zadani barvy pozadi
#barvaPozadi = input('Zadejte barvu pozadi: ')


# preddefinovani parametru
#delka = 2                          
#uhel = 90                           

# funkce pro vykresleni draci krivky
def Krivka(val, delka, uhel):              
     """Vykresleni krivky.
     >>> Krivka()
     """
     if val == 0:
        turtle.forward(delka)              
     else:
         Krivka(val - 1, delka, 90)         
         turtle.left(uhel)
         Krivka(val - 1, delka, -90)       
     
       
#Nastaveni poctu iteraci
def vrat_cislo(iterace):
    """Vrat cislo.
    
    >>> vrat_cislo('12')
    '12'
    """
    try:
        val = int(iterace)              # ulozeni hodnoty, kterou zada uzivatel
        if val < 0:                     # pokud je zadane cislo zaporne nastavi se kladna hodnota zadaneho cisla
            val = val * -1
  
    except ValueError:                  # pokud hodnota neni cislo nastavi vychozi hodnotu iteraci na 9
        val = 9
    
    return val


# funkce pro nastaveni barvy pera 
def nbp():
    """Nastav barvu pera.
    >>> nbp()
    """
    try:
     turtle.color(barvaPera)
     if barvaPera == str(''):                                  # pokud je hodnota retezce prazdna, nastavi se barva pera na cervenou
         turtle.color('red') 
    except (turtle.TurtleGraphicsError, _tkinter.TclError):    # pokud je hodnota retezce neplatna (barva neexistuje a nastatne error), zachyti tuto chybu a nastavi barvu pera na cervenou
        turtle.color('red') 

    

# funkce pro nastaveni barvy pozadi
def nbpo():
    """Nastav barvu pozadi.
    >>> nbpo()
    """
    try:
      turtle.bgcolor(barvaPozadi)
      if barvaPozadi == str(''):                            # pokud je hodnota retezce prazdna, nastavi se barva pozadi na cernou
          turtle.bgcolor('black') 
    except (turtle.TurtleGraphicsError, _tkinter.TclError):
        turtle.bgcolor('black')                             # pokud je hodnota retezce neplatna (barva neexistuje a nastatne error), zachyti tuto chybu a nastavi barvu pozadi na cernou
     




# funkce pro nasstaveni vykreslovaci plochy
def nastav_prostredi():
    # nastaveni prostredi
    turtle.Screen().clear()
    turtle.speed(0 )
    turtle.pensize(1)

    # pocatecni bod vykreslovani
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()

parametry()
nastav_prostredi()
nbp()
nbpo()

# zavolani funkce Krivka
Krivka(vrat_cislo(iterace), delka, uhel)

turtle.done()