"""Overeni prvocisel.

Program obsahuje funkci pro mereni casu potrebneho k dokonceni behu.
Obsahuje jednoduche funkce pro overeni, zda je zadane cislo prvocislem
a vraci vysledek na konzoli.
"""


def isPrime(n):
    """Hlavni overovaci funkce."""
    # vylouceni zapornych cisel, nuly a jednicky
    if n <= 1:
        return False

    # potvrzeni cisel 2, 3
    if n <= 3:
        return True

    # vylouceni sudych cisel a cisel delitelnych 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Vsechna prvocisla jsou ve tvaru 6n +/-1
    # Use P = 6k +/- 1 to allow iterating by 6
    i = 5
    while i * i <= n:

        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
