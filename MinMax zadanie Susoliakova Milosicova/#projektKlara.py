#projektKlara


# Uživatel vloží čísla
        
x = input('Vložte libovolný počet celých čísel oddělených mezerami: ')
print("\n")

cisla_uzivatele = x.split()
print('seznam čísel: ', cisla_uzivatele)

print ("Nejvyšší hodnota v seznamu: ", max(cisla_uzivatele))
print ("Nejmenší hodnotu v seznamu: ", min(cisla_uzivatele))


cisla_uzivatele.index(6) # will return 1


# 1. Vygeneruj nahodne n cisel random

# import random
# nahodna_cisla = random.sample(range(-50, 50), 20)
# print(nahodna_cisla)

# print ("Nejvyšší hodnota v seznamu: ", max(nahodna_cisla))
#  print ("Nejmenší hodnotu v seznamu: ", min(nahodna_cisla))


