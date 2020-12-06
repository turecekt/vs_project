# Author:   Barbana Klimekova <b_klimekova@utb.cz>
#           Lucia Kubaskova <l_kubaskova@utb.cz>
#           Tomas_Prikasky <t_prikasky@utb.cz>
#
# Description:  Create a program to evaluate whether the entered number is a prime number.
#               Prime numbers have exactly two divisors, are divisible by only 1 and by themselves.

class PrimeNumber:
    """Class for o evaluate whether the entered number is a prime number."""

number = input("Vlož číslo: ")
if number.isdigit() and int(number) > 0:
    number = int(number)
    divisors = []
    count = 0

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
            count += 1
            if count > 2:
                break
    if count == 2:
        print(f"delitelia: {divisors}")
        print(f"Číslo {number} je prvočíslo")
    else:
        print(f"delitelia: {divisors}")
        print(f"Číslo {number} není prvočíslo")

else:
    print("Nebylo zadáno kladné číslo")