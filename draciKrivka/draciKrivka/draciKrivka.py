
# Naimportovani turtle modulu pro pouziti grafiky
import turtle



## vyzve uzivatele pro zadani poctu iteraci
#iterace = input('Zadejte pocet iteraci: ')

## vyzve uzivatele pro zadani barvy pera
#barvaPera = input('Zadejte barvu pera: ')

## vyzve uzivatele pro zadani barvy pozadi
#barvaPozadi = input('Zadejte barvu pozadi: ')

# funkce pro vykresleni draci krivky
def Krivka(val, delka, uhel):               # nazev funkce a vstupni parametry
     if val == 0:
        turtle.forward(delka)               # vykresli caru
     else:
         Krivka(val - 1, delka, 90)         # otoceni o 90 stupnu mezi carami
         turtle.left(uhel)
         Krivka(val - 1, delka, -90)        # otoceni o 90 stupnu mezi carami
     
       
# nastaveni prostredi
def nastaveni():
    turtle.Screen().clear()
    turtle.speed(0 )
    turtle.pensize(1)

    # pocatecni bod vykreslovani
    turtle.penup()
    turtle.goto(100, 100)
    turtle.pendown()


##zachyceni vstupu pro iterace
#def vrat_cislo():
#    try:
#        val = int(iterace)              # ulozeni hodnoty, kterou zada uzivatel
#        if val < 0:                     # pokud je zadane cislo mensi jak 0 nastavi se vychozi hodnota iteraci na 9
#            val = 9
  
#    except ValueError:                  # pokud hodnota neni cislo nastavi vychozi hodnotu iteraci na 9
#        val = 9
    
#    return val


## funkce pro nastaveni barvy pera 
#def nbp():
#    if barvaPera:
#        turtle.color(barvaPera)       
#    else:
#        turtle.color('red')             # pokud uzivatel necha pole prazdne, nastavi se vychozi barva cervena


## funkce pro nastaveni barvy pozadi
#def nbpo():
#     if barvaPozadi:
#        turtle.bgcolor(barvaPozadi)

#     else:
#        turtle.bgcolor('black')         # pokud uzivatel necha pole prazdne, nastavi se vychozi barva cerna
     

# preddefinovane parametry
delka = 2                           # delka cary, ktera se vykresli
uhel = 90                           # uhel mezi rekurzemi



#nbp()
#nbpo()

# zavolani funkce Krivka
nastaveni()
Krivka(9, delka, uhel)

turtle.done()