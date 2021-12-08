from isPrime import isPrime

# Get user input and run isPrime
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a number: "))
            result = "Is Prime? "
            break
        except ValueError:
            print("Please enter an integer.")

    print(result + str(isPrime(n)))
