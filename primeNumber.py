number = input("Vlož číslo: ")
if number.isdigit() and int(number) > 0:
    number = int(number)
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    print(f"delitelia: {divisors}")
    if len(divisors) == 2:
        print(f"Číslo {number} je prvočíslo")
    else:
        print(f"Číslo {number} není prvočíslo")

else:
    print("Nebylo zadáno kladné číslo")