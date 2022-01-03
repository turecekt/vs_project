import fcie_temp

# Uživatel zvolí, o jaké pole čísel se bude jednat
print('Zvol cislo')
print('- 1: Vygeneruj nahodne 20 cisel random  \n')
print('- 2: Vložte libovolný počet celých čísel oddělených mezerami  \n')
print('- 3: Nacitaj zo suboru cisla  \n')

choice = int(input('Enter your choice:'))

fcie_temp.main_program(choice)
