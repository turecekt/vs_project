
# Naimportovani turtle modulu pro pouziti grafiky
import turtle

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
     
       
# nastaveni prostredi
turtle.Screen().clear()
turtle.speed(0 )
turtle.pensize(1)

# pocatecni bod vykreslovani
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()


#zachyceni vstupu pro iterace
try:
    val = int(iterace)              # ulozeni hodnoty, kterou zada uzivatel
    if val < 0:                     # pokud je zadane cislo mensi jak 0 nastavi se vychozi hodnota iteraci na 9
        val = 9
except ValueError:                  # pokud hodnota neni cislo nastavi vychozi hodnotu iteraci na 9
    val = 9

if barvaPera:
    turtle.color(barvaPera)         # pokud uzivatel necha pole prazdne, nastavi se vychozi barva cervena
else:
    turtle.color('red')
# podminka pro barvu pozadi
if barvaPozadi:
    turtle.bgcolor(barvaPozadi)
else:
    turtle.bgcolor('black')         # pokud uzivatel necha pole prazdne, nastavi se vychozi barva cerna
    

# preddefinovane parametry
delka = 2                           # delka cary, ktera se vykresli
uhel = 90                           # uhel mezi rekurzemi


# zavolani funkce Krivka
Krivka(val, delka, uhel)

turtle.done()