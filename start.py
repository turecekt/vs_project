"""Hlavni cast programu pro potvrzeni prvocisla.

Na konzoli vypise zadost o zadani cisla
po zadani potvrdi, zda se jedna o prvocislo nebo ne.
"""

from hlavniFunkce import isPrime

if __name__ == "__main__":
    while True:
        try:  # uzivatelsky vstup
            n = int(input("Enter a number: "))
            result = "Is Prime? "
            break
        except ValueError:
            print("Please enter an integer.")

    print(result + str(isPrime(n)))  # zobrazeni vysledku
