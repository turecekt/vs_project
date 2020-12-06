number = input("Vlož číslo: ")
if number.isdigit() and int(number) > 0:
    number = int(number)
    divisors = []

else:
    print("Nebylo zadáno kladné číslo")