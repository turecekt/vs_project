"""Hlavni cast programu pro potvrzeni prvocisla.

Na konzoli vypise zadost o zadani cisla
po zadani potvrdi, zda se jedna o prvocislo nebo ne.
"""

from hlavniFunkce import isPrime

if __name__ == "__main__":
    while True:
        try:  # uzivatelsky vstup
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter an integer.")

    print("Is " + str(n) + " Prime number? " + str(isPrime(n)))  # zobrazeni vysledku
