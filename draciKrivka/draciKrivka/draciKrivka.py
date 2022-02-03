
"""Heighway Dragon."""

# Naimportovani turtle modulu pro pouziti grafiky a _tkinter
# pro vymezeni vyjimek u funkci
import turtle
import _tkinter

print('Seznam dostupnych barev: blue, green, red, cyan, megenta, yellow, white, black')      
       
#Nastaveni poctu iteraci
def vrat_cislo(iterace):
    """Vrat cislo.
    
    >>> vrat_cislo('12')
    12
    """
    try:
        val = int(iterace)              
        # ulozeni hodnoty, kterou zada uzivatel
        if val < 0:                     
        # pokud je zadane cislo zaporne nastavi se kladna hodnota zadaneho cisla
            val = val * -1
  
    except ValueError:                  
        # pokud hodnota neni cislo nastavi vychozi hodnotu iteraci na 9
        val = 9
    
    return val


# funkce pro nastaveni barvy pera 
def nbp(barvaPera):
    """Nastav barvu pera."""
    try:
     turtle.color(barvaPera)
     if barvaPera == str(''):                                  
         # pokud je hodnota retezce prazdna, nastavi se barva pera na cervenou
         turtle.color('red') 
    except (turtle.TurtleGraphicsError, _tkinter.TclError):    
        # pokud je hodnota retezce neplatna (barva neexistuje a nastatne
        # error), zachyti tuto chybu a nastavi barvu pera na cervenou
        turtle.color('red') 

    

# funkce pro nastaveni barvy pozadi
def nbpo(barvaPozadi):
    """Nastav barvu pozadi."""
    try:
      turtle.bgcolor(barvaPozadi)
      if barvaPozadi == str(''):                            
          # pokud je hodnota retezce prazdna, nastavi se barva pozadi na cernou
          turtle.bgcolor('black') 
    except (turtle.TurtleGraphicsError, _tkinter.TclError):
        turtle.bgcolor('black')                             
        # pokud je hodnota retezce neplatna (barva neexistuje a nastatne
        # error), zachyti tuto chybu a nastavi barvu pozadi na cernou
     

# funkce pro vykresleni draci krivky
def Krivka(val, delka, uhel):              
     """Vykresleni krivky."""
     if val == 0:
        turtle.forward(delka)              
     else:
         Krivka(val - 1, delka, 90)         
         turtle.left(uhel)
         Krivka(val - 1, delka, -90)    


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


if __name__ == '__main__':
    iterace = input('Zadejte pocet iteraci: ')
    barvaPera = input('Zadejte barvu pera: ')
    barvaPozadi = input('Zadejte barvu pozadi: ')
    delka = 2
    uhel = 90
    nastav_prostredi()
    nbp(barvaPera)
    nbpo(barvaPozadi)
    # zavolani funkce Krivka
    Krivka(vrat_cislo(iterace), delka, uhel)
    turtle.done()