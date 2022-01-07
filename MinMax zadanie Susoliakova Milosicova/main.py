"""Hlavne funkcie na spustanie hlavneho programu."""


def main_program(choiceForField):
    """Program vytvoří pole náhodných čísel."""
    if (choiceForField == 1):
        print('\nChoice 1: Vygeneruj nahodne 20 cisel random')
        import random
        nahodna_cisla = random.sample(range(-50, 50), 20)
        print(nahodna_cisla)
        # Uživatel nahraje jednotlivá čísla do programu
        return nahodna_cisla
    elif (choiceForField == 2):
        print('\nChoice 2:')
        x = input('Vložte libovolný počet celých čísel oddělených mezerami: ')
        cisla_uzivatele = x.split()
        print('Seznam čísel: ', cisla_uzivatele)
        # Program vybere čísla zadane od uzivatela
        return cisla_uzivatele
    elif (choiceForField == 3):
        print('\nChoice 3: Nacitaj zo suboru cisla')
        f = open(
                'vs_project/MinMax zadanie Susoliakova Milosicova/cisla.txt',
                'r')
        with f as tf:
            cisla = tf.read().split(',')
        # Program vybere čísla z textového dokumentu file.txt
        f.close()
        return cisla


def vyber_algorythm(choice_algorythm, cisla):
    """Uživatel si zvolil sort choice_algorythm."""
    # Importování pro práci s časováním
    import time
    # Importování funkcí pro sortování
    import sorts

    if (choice_algorythm == 1):
        sorts.buble_sort(cisla)
        print("Buble Sort Sorted array: " + str(cisla))
    elif (choice_algorythm == 2):
        sorts.merge_sort(cisla, 0, len(cisla) - 1)
        print("Merge Sort Sorted array: " + str(cisla))
    elif (choice_algorythm == 3):
        sorts.insertion_sort(cisla)
        print("Insertion Sort Sorted array: " + str(cisla))
    elif (choice_algorythm == 4):
        sorts.quick_sort(cisla, 0, len(cisla) - 1)
        print("Quick Sort Sorted array: " + str(cisla))
    elif (choice_algorythm == 5):
        print('All Sorts\n')
        original_array = cisla
        buble_array = original_array
        merge_array = original_array
        insertion_array = original_array
        quick_array = original_array

        print('Execution time in seconds for:')

        # Výpis danných sortů a jejich času trvání řazení
        startTime = time.time()
        sorts.buble_sort(buble_array)
        executionTime = (time.time() - startTime)
        print('Buble sort: ' + str(executionTime))

        startTime1 = time.time()
        sorts.merge_sort(merge_array, 0, len(merge_array) - 1)
        executionTime = (time.time() - startTime1)
        print('Merge sort ' + str(executionTime))

        startTime2 = time.time()
        sorts.insertion_sort(insertion_array)
        executionTime = (time.time() - startTime2)
        print('Insertion sort: ' + str(executionTime))

        startTime3 = time.time()
        sorts.quick_sort(quick_array, 0, len(quick_array) - 1)
        executionTime = (time.time() - startTime3)
        print('Quick sort ' + str(executionTime))

        print("Sorted array: " + str(merge_array))


# Implementační funkce
def min_max_index(cisla_uzivatele):
    """Funkcia najde min a max zadaneho pola cisel."""
    max_cislo = max(cisla_uzivatele)
    min_cislo = min(cisla_uzivatele)

    # Určí nejvyšší a nejnižší hodnotu v poli

    print("\nNejvyšší hodnota v seznamu: ", max_cislo)
    print("Nejmenší hodnotu v seznamu: ", min_cislo)

    # Určí pořadí čísla v poli
    print("Index pro: ")
    print("- nejvyšší hodnota v seznamu: ", cisla_uzivatele.index(max_cislo))
    print("- nejmensi hodnota v seznamu: ", cisla_uzivatele.index(min_cislo))
    print("\n")


def chooseSorts():
    """Funkcia na zvolenie sortu pre dane pole."""
    print('\nZvol cislo')
    print('1. Bubble Sort')
    print('2. Merge Sort')
    print('3. Insertion Sort')
    print('4. Quick Sort')
    print('5. All Sorts')

    choice_algorythm = int(input('Enter your choice:'))

    return choice_algorythm


def main():
    """Uživatel zvolí, o jaké pole čísel se bude jednat."""
    print('Zvol cislo')
    print('- 1: Vygeneruj nahodne 20 cisel random')
    print('- 2: Vložte libovolný počet celých čísel oddělených mezerami')
    print('- 3: Nacitaj zo suboru cisla')
    choiceForField = int(input('Enter your choice:'))

    if((choiceForField != 1) and (choiceForField != 2)
            and (choiceForField != 3)):
        return print("Incorrect input!")
    else:
        choice_algorythm = chooseSorts()

        if((choice_algorythm != 1) and (choice_algorythm != 2)
                and (choice_algorythm != 3)
                and (choice_algorythm != 4)
                and (choice_algorythm != 5)):
            return print("Incorrect input!")
        else:
            field_number = main_program(choiceForField)
            # najdenie min, max cisla v poli "cisla" a najde je v indexu
            min_max_index(field_number)
            vyber_algorythm(choice_algorythm, field_number)


if __name__ == "__main__":
    main()
