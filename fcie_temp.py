from sorts import insertion_sort

def main_program(choice):

    # Program vytvoří pole náhodných čísel
    if (choice == 1):
        print('Choice 1: Vygeneruj nahodne 20 cisel random \n')

        import random
        nahodna_cisla = random.sample(range(-50, 50), 20)
        
        print(nahodna_cisla)

        # Uživatel nahraje jednotlivá čísla do programu
        vyber_algorythm(nahodna_cisla)

    if (choice == 2):
        print('Choice 2\n')
                
        x = input('Vložte libovolný počet celých čísel oddělených mezerami: ')
        print("\n")

        cisla_uzivatele = x.split()
        print('Seznam čísel: ', cisla_uzivatele)
        
        # Program vybere čísla zadane od uzivatela 
        vyber_algorythm(cisla_uzivatele)


    if (choice == 3):
        print('Nacitaj zo suboru cisla \n')

        with open("file.txt", "r") as tf:
            cisla = tf.read().split(',') 

        # Program vybere čísla z textového dokumentu file.txt
        vyber_algorythm(cisla)


def vyber_algorythm(cisla):

    # najdenie min, max cisla v poli "cisla" a najde je v indexu

    min_max_index(cisla)

    # Uživatel si zvolí sort

    print('Zvol cislo \n')
    print('1. Bubble Sort  \n')
    print('2. Merge Sort  \n')
    print('3. Insertion Sort  \n')   
    print('4. Quick Sort  \n')   
    print('5. All Sorts  \n')   

    choice = int(input('Enter your choice:'))

    # Importování pro práci s časováním

    import time

    # Importování funkcí pro sortování

    import sorts

    if (choice == 1):
        print('Choice 1\n')

        sorts.buble_sort(cisla)
        print("Sorted array: " + str(cisla))

    if (choice == 2):
        print('Choice 2\n')

        sorts.merge_sort(cisla, 0, len(cisla) -1)
        print("Sorted array: " + str(cisla))
    if (choice == 3):
        print('Choice 3\n')

        sorts.insertion_sort(cisla)
        print("Sorted array: " + str(cisla))
    if (choice == 4):
        print('Choice 4\n')
        sorts.quick_sort(cisla, 0, len(cisla) - 1)
        print("Sorted array: " + str(cisla))
    if (choice == 5):
        print('Choice 5\n')

        import time
        
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
        sorts.merge_sort(merge_array, 0, len(merge_array) -1)
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

    max_cislo =  max(cisla_uzivatele)
    min_cislo = min(cisla_uzivatele)

     # Určí nejvyšší a nejnižší hodnotu v poli

    print ("Nejvyšší hodnota v seznamu: ", max_cislo)
    print ("Nejmenší hodnotu v seznamu: ", min_cislo)

     # Určí pořadí čísla v poli

    print ("Index pro nejvyšší hodnota v seznamu: ", cisla_uzivatele.index( max_cislo))
    print ("Index pro nejmensi hodnota v seznamu: ", cisla_uzivatele.index( min_cislo))   

