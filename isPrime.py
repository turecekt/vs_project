import time

def isPrime(n):
    start = time.time()

    def printTime(start):
        print("\rFinished in %f seconds" % (time.time() - start))

    # Elimitate trivial cases
    if n <= 1:
        printTime(start)
        return False
    if n <= 3:
        printTime(start)
        return True
    if n % 2 == 0 or n % 3 == 0:
        printTime(start)
        return False

    # Use the fact that all primes are of the form 6k +/- 1 to allow iterating by 6
    i = 5
    while i * i <= n:
        progress = i*i/n
        print("\r%f%%" % (i*i/n*100), end="")

        if n % i == 0 or n % (i + 2) == 0:
            printTime(start)
            return False
        i += 6

    printTime(start)
    return True

# Get user input and run isPrime
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter an integer.")

    print(isPrime(n))

