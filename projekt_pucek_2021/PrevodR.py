# Metoda pro převod z arabských čísel na římská
def narim(nrcislo):
    if 4000 > nrcislo > 0:
        # List hodnot, použitých při převodu
        hod = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # List obsahující možné symboly a kombinace vyjímek
        sym = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
        nrrimske = ''
        i = 0
        # Dokud nejsou převedeny všechny čísla, provádí se převod
        while nrcislo > 0:
            for _ in range(nrcislo // hod[i]):
                nrrimske += sym[i]
                nrcislo -= hod[i]
            i += 1
        return nrrimske
        # Návratová hodnota výsledku
    # Pokud není splněna podmínka, program zahlásí chybu
    else:
        print("Chybně zadané číslo.")
        return " "  # Vrátí zpět pouze mezeru


# Metoda pro převod z římských čísel na arabské
def naar(s):
    # Podmínka pro ošetření vstupu při vložení prázdné hodnoty
    if s != 0:
        # Seznam možných symbolů a vyjímek při převodu
        symr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        j = 0
        nacislo = 0
        # Cyklus, který opakuje, dokud proměnná j
        # není menší, než délka vstupního stringu
        while j < len(s):
            # Podmínka pro převod vyjímek ze seznamu výše
            if j + 1 < len(s) and s[j:j + 2] in symr:
                nacislo += symr[s[j:j + 2]]
                j += 2
            # Pokud se nenachází vyjímka pro
            # převod, provede se klasický jednočíselný
            else:
                nacislo += symr[s[j]]
                j += 1
        return nacislo  # Návratová hodnota výsledku
    # Je-li odeslána prázdná hodnota římského čísla, program zahlásí chybu
    else:
        print("Chybně zadané číslo.")
        return 0
