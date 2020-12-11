print('===Program pro posouzeni cisla / prvocisla===')
cislo = int(input('Zadejte libovolne cele cislo k posouzeni: '))
    # program pro urceni prvocisla                          # pro cislo > 1
if cislo > 1:
    for i in range(2,cislo):
        if (cislo % i) == 0:                    # cislo nedává zbytek po dělení
            print(cislo ,' neni prvocislo.')
            print(i ,' * ', cislo//i, ' = ', cislo)    # důkaz dělitelnosti
            print('(Pro vypocet byla pouzita deterministicka metoda.)')
            break
    else:                                       # cislo dává zbytek po dělení
            print(cislo ,' je prvocislo.')
            print('(Pro vypocet byla pouzita deterministicka metoda.)')
elif cislo < 0:                                       # pro cislo <= 1
    print('Zadane cislo musi byt > 0.')
elif cislo == 1:
    print('Cislo 1 neni prvocislo dle definice.')
else:
    print(cislo ,' neni prvocislo.')
    print('(Pro vypocet byla pouzita deterministicka metoda.)')
        
# print('(Pro vypocet byla pouzita deterministicka metoda.)')
# deterministicka metoda = vysledek je pokazde stejny a je urcen dle definice prvocisel
# algoritmus je predvitatelny
