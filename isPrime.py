"""Overeni prvocisel.

Program obsahuje funkci pro mereni casu potrebneho k dokonceni behu.
Obsahuje jednoduche funkce pro overeni, zda je zadane cislo prvocislem
a vraci vysledek na konzoli.
"""


# import time

# PRINT_TIMINGS = False


def isPrime(n):
    """Hlavni overovaci funkce."""
    """start = time.time()

    def printTime(start):
        if PRINT_TIMINGS:
            print("\rFinished in %f seconds" % (time.time() - start))

    def printProgress(i):
        if PRINT_TIMINGS:
            print("\r%f%%" % (i*i/n*100), end="")
"""
    # vylouceni zapornych cisel, nuly a jednicky
    if n <= 1:
#        printTime(start)
        return False

    # potvrzeni cisel 2, 3
    if n <= 3:
#        printTime(start)
        return True

    # vylouceni sudych cisel a cisel delitelnych 3
    if n % 2 == 0 or n % 3 == 0:
#        printTime(start)
        return False

    # Vsechna prvocisla jsou ve tvaru 6n +/-1
    # Use P = 6k +/- 1 to allow iterating by 6
    i = 5
    while i * i <= n:
#        printProgress(i)

        if n % i == 0 or n % (i + 2) == 0:
#            printTime(start)
            return False
        i += 6

#    printTime(start)
    return True
