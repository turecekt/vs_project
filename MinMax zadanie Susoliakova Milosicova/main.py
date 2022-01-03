import fcie_temp;

# Uživatel zvolí, o jaké pole čísel se bude jednat

print('Zvol cislo 1: Vygeneruj nahodne 20 cisel random  \n')
print('Zvol cislo 2: Vložte libovolný počet celých čísel oddělených mezerami  \n')
print('Zvol cislo 3: Nacitaj zo suboru cisla  \n')

choice = int(input('Enter your choice:'))

fcie_temp.main_program(choice)


