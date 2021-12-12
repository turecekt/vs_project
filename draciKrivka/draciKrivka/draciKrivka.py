
# Naimportovani turtle modulu pro pouziti grafiky a _tkinter pro vymezeni vyjimek u funkci
import turtle
import _tkinter

# definovani promennych z inputu uzivatele
# vyzve uzivatele pro zadani poctu iteraci
iterace = input('Zadejte pocet iteraci: ')

# vyzve uzivatele pro zadani barvy pera
barvaPera = input('Zadejte barvu pera: ')

# vyzve uzivatele pro zadani barvy pozadi
barvaPozadi = input('Zadejte barvu pozadi: ')


# funkce pro vykresleni draci krivky
def Krivka(val, delka, uhel):               # nazev funkce a vstupni parametry
     if val == 0:
        turtle.forward(delka)               # vykresli caru
     else:
         Krivka(val - 1, delka, 90)         # otoceni o 90 stupnu mezi carami
         turtle.left(uhel)
         Krivka(val - 1, delka, -90)        # otoceni o 90 stupnu mezi carami
     
       
#zachyceni vstupu pro iterace
def vrat_cislo():
    try:
        val = int(iterace)              # ulozeni hodnoty, kterou zada uzivatel
        if val < 0:                     # pokud je zadane cislo zaporne nastavi se kladna hodnota zadaneho cisla
            val = val * -1
  
    except ValueError:                  # pokud hodnota neni cislo nastavi vychozi hodnotu iteraci na 9
        val = 9
    
    return val


# funkce pro nastaveni barvy pera 
def nbp():
    try:
     turtle.color(barvaPera)
     if barvaPera == str(''):                                  # pokud je hodnota retezce prazdna, nastavi se barva pera na cervenou
         turtle.color('red') 
    except (turtle.TurtleGraphicsError, _tkinter.TclError):    # pokud je hodnota retezce neplatna (barva neexistuje a nastatne error), zachyti tuto chybu a nastavi barvu pera na cervenou
        turtle.color('red') 

    

# funkce pro nastaveni barvy pozadi
def nbpo():
    try:
      turtle.bgcolor(barvaPozadi)
      if barvaPozadi == str(''):                            # pokud je hodnota retezce prazdna, nastavi se barva pozadi na cernou
          turtle.bgcolor('black') 
    except (turtle.TurtleGraphicsError, _tkinter.TclError):
        turtle.bgcolor('black')                             # pokud je hodnota retezce neplatna (barva neexistuje a nastatne error), zachyti tuto chybu a nastavi barvu pozadi na cernou
     

# preddefinovane parametry
delka = 2                           # delka cary, ktera se vykresli
uhel = 90                           # uhel mezi rekurzemi


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

nastav_prostredi()
nbp()
nbpo()

# zavolani funkce Krivka
Krivka(vrat_cislo(), delka, uhel)

turtle.done()